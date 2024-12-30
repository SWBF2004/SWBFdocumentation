import re
from pathlib import Path
from md.nodes import Node, Document, Text, Heading, List, ListItem, Image, Reference, Code, Table, TableRow, TableCell
from md.token import Token, TK
from md.iterator import Iterator


class Parser(Iterator):
    RE_ALGINMENT = re.compile('((:?-+:?)+)')

    class State:
        Start, \
        List, \
        Table \
            = range(3)

    def __init__(self, file: Path, tokens: list):
        super().__init__(tokens)

        self.file: Path = file
        self.root: Document = Document(file)
        self.curr: Node = self.root
        self.state: list = [Parser.State.Start]

        # Current Node
        self.nbeg: int = 0
        self.nend: int = 0

    def consume(self, type: TK):
        if self.get() and self.get().type == type:
            self.next()
            return True
        return False

    def consume_strict(self, type: TK):
        if not self.consume(type):
            self.error(type)

    def consume_any(self, types: list):
        if self.get() and self.get().type in types:
            self.next()
            return True
        return False

    def consume_until(self, type: TK):
        while self.get() and self.get().type != type:
            self.next()
    
    def discard(self):
        self.next()
        self.collect_tokens()

    def collect_tokens(self):
        self.nbeg = self.nend  # End of last node
        self.nend = self.pos  # End of current node
        return self.buffer[self.nbeg:self.nend]

    def error(self, expected: TK):
        nl = '\n'
        t: Token = self.get()
        tokens = self.buffer[self.nend:self.pos + 1]
        text = "".join(list(map(lambda x: x.text, tokens)))
        indent = len(text[text.rfind(nl)]) if text.find('\n') > -1 else len(text) - len(tokens[-1].text)

        msg = f'\n\n{self.file.absolute()}: Line {t.row} Col {t.col}\n\n'
        msg += f'{text}\n'
        msg += f'{indent * " "}{"^" * len(self.get().text)}\n\n'
        msg += f'Expected \'{expected}\' got \'{tokens[-1].text}\'\n'

        raise Exception(msg)

    def parse(self):
        while self:
            self.parse_nodes()
        
        return self.root

    def parse_nodes(self):
        if self.state[-1] == Parser.State.Start:

            if self.get().type == TK.NumberSign:
                self.parse_heading()
            elif self.get().type == TK.Minus:
                self.parse_list()
            elif self.get().type == TK.ExclamationMark:
                self.parse_image()
            elif self.get().type == TK.SquareBracketOpen:
                self.parse_reference()
            elif self.get().type == TK.Backtick:
                self.parse_code()
            elif self.get().type == TK.VerticalBar:
                self.parse_table()
            elif self.get().type in [TK.LineFeed, TK.Space]:
                # Discard newline or space at the start of a line
                self.discard()
            elif self.get().type in TK.Text:
                self.parse_text()
            else:
                self.error(TK.Null)

        elif self.state[-1] == Parser.State.List:
            if self.get().type == TK.SquareBracketOpen:
                self.parse_reference()
            elif self.get().type == TK.Backtick:
                self.parse_code()
            elif self.get().type == TK.Minus:
                self.parse_list()
            elif self.get().type == TK.Space:
                # Discard spaces at the start of the line
                self.discard()
            elif self.get().type in TK.Text:
                self.parse_text()
            else:
                self.error(TK.Null)
        
        elif self.state[-1] == Parser.State.Table:
            if self.get().type in TK.Text:
                self.parse_text()
            elif self.get().type == TK.ExclamationMark:
                self.parse_image()
            elif self.get().type == TK.SquareBracketOpen:
                self.parse_reference()
            elif self.get().type == TK.Backtick:
                self.parse_code()
            elif self.get().type == TK.VerticalBar:
                return
            else:
                self.error(TK.Null)

    def parse_text(self):
        while self.consume_any(TK.Text):
            pass

        self.curr.add(Text(self.collect_tokens()))

    def parse_heading(self):
        self.consume_until(TK.LineFeed)

        self.curr.add(Heading(self.collect_tokens()))

        
    def parse_image(self):
        self.consume_strict(TK.ExclamationMark)

        self.consume_strict(TK.SquareBracketOpen)

        while self.consume_any(TK.ReferenceText):
            pass

        self.consume_strict(TK.SquareBracketClose)

        self.consume_strict(TK.ParanthesisOpen)

        while self.consume_any(TK.TargetName):
            pass

        self.consume_strict(TK.ParanthesisClose)

        self.curr.add(Image(self.collect_tokens()))

    def parse_reference(self):
        self.consume_strict(TK.SquareBracketOpen)

        while self.consume_any(TK.ReferenceText):
            pass

        self.consume_strict(TK.SquareBracketClose)

        self.consume_strict(TK.ParanthesisOpen)

        while self.consume_any(TK.TargetName):
            pass

        self.consume_strict(TK.ParanthesisClose)

        self.curr.add(Reference(self.collect_tokens()))

    def parse_code(self):
        is_block = False

        self.consume(TK.Backtick)

        if self.consume(TK.Backtick):
            self.consume_strict(TK.Backtick)

            is_block = True

        t = self.get()
        while t.type != TK.Backtick:
            t = self.next()

        t = self.next()

        if is_block:
            self.consume_strict(TK.Backtick)
            self.consume_strict(TK.Backtick)

        self.curr.add(Code(self.collect_tokens()))

    def parse_list(self):
        self.state.append(Parser.State.List)

        list_root = List(None)
        self.curr.add(list_root)
        self.curr = list_root

        while self and self.get().type != TK.LineFeed:
            self.parse_list_item()

            # Discard line feed
            self.discard()
        
        self.curr = list_root.parent
        self.state.pop()

    def parse_list_item(self):
        list_item = ListItem(None)
        self.curr.add(list_item)
        self.curr = list_item

        # Discard list start
        self.discard()

        while self and self.get().type != TK.LineFeed:
            self.parse_nodes()

        self.curr = list_item.parent
        self.consume_until(TK.LineFeed)

        self.curr = list_item.parent

    def parse_table(self):
        self.state.append(Parser.State.Table)

        table = Table(None)
        self.curr.add(table)
        self.curr = table

        while self and self.get().type != TK.LineFeed:
            self.parse_table_row()

            # Discard line feed
            self.discard()

        if len(table.children) > 0:
            table.columns = len(table.children[0].children)

        if len(table.children) > 1:
            for cell in table.children[1].children:
                if len(cell.children) > 0 and hasattr(cell.children[0], 'text'):
                    text = cell.children[0].text
                    if re.search(r':-{3,}:', text):
                        table.cell_alignment.append(Table.Align.center)
                    elif text.find('---:') > -1:
                        table.cell_alignment.append(Table.Align.right)
                    else:
                        table.cell_alignment.append(Table.Align.left)

        if table.cell_alignment:
            table.children.pop(1)
        else:
            table.cell_alignment = [Table.Align.left] * table.columns
        

        self.curr = table.parent

        self.state.pop()

    def parse_table_row(self):
        row = TableRow(None)
        self.curr.add(row)
        self.curr = row

        # Discard row start
        self.discard()

        while self and self.get().type != TK.LineFeed:
            self.parse_table_cell()

            # Discard cell separator or row end
            self.discard()

        self.curr = row.parent

    def parse_table_cell(self):
        cell = TableCell(None)
        self.curr.add(cell)
        self.curr = cell

        while self and self.get().type != TK.VerticalBar:
            self.parse_nodes()

        self.curr = cell.parent
