import re
from pathlib import Path
from util.nodes import Node, Document, LexicalNode
from util.token import Token, TK
from util.parser import Parser


class Text(LexicalNode):
    def __init__(self, tokens: list, parent: Node = None):
        super().__init__(tokens, parent)

        self.text = self.raw().strip()


class Heading(Node):
    def __init__(self, parent: Node = None):
        super().__init__(parent)

        self.level = 1


class Image(LexicalNode):
    RE = re.compile(r'\!\[(.*)\]\((.*)\)')

    def __init__(self, tokens: list, parent: Node = None):
        super().__init__(tokens, parent)

        match = re.search(Image.RE, self.raw())

        self.text = match.group(1)
        self.target = match.group(2)


class Reference(LexicalNode):
    RE = re.compile(r'\[(.*)\]\((.*)\)')

    def __init__(self, tokens: list, parent: Node = None):
        super().__init__(tokens, parent)

        match = re.search(Reference.RE, self.raw())

        self.text = match.group(1)
        self.target = match.group(2)


class Code(LexicalNode):
    RE = re.compile('`([^`]*)`')

    def __init__(self, tokens: list, parent: Node = None):
        super().__init__(tokens, parent)

        match = re.search(Code.RE, self.raw())

        self.text = match.group(1)


class List(Node):
    def __init__(self, parent: Node = None):
        super().__init__(parent)


class ListItem(Node):
    def __init__(self, parent: Node = None):
        super().__init__(parent)


class Table(Node):
    class Align:
        left = 'left'
        center = 'center'
        right = 'right'

    def __init__(self, parent: Node = None):
        super().__init__(parent)

        self.columns = 0
        self.cell_alignment = []


class TableRow(Node):
    def __init__(self, parent: Node = None):
        super().__init__(parent)


class TableCell(Node):
    def __init__(self, parent: Node = None):
        super().__init__(parent)



class MD(Document, Parser):
    RE_ALGINMENT = re.compile('((:?-+:?)+)')

    class State:
        Start, \
        Heading, \
        List, \
        Table \
            = range(4)

    def __init__(self, filepath: Path, tokens: list[Token]):
        super().__init__(filepath=filepath, tokens=tokens)

        self.curr: Node = self
        self.state: list[MD.State] = [MD.State.Start]

        # Current Node
        self.nbeg: int = 0
        self.nend: int = 0

    def parse(self):
        while self:
            self.parse_nodes()

        return self

    def parse_nodes(self):
        if self.state[-1] == MD.State.Start:

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
                self.discard()  # Discard newline or space at the start of a line
            elif self.get().type in TK.Text:
                self.parse_text()
            else:
                self.error(TK.Null)

        elif self.state[-1] == MD.State.Heading:
            if self.get().type == TK.SquareBracketOpen:
                self.parse_reference()
            elif self.get().type == TK.Backtick:
                self.parse_code()
            elif self.get().type in TK.Text:
                self.parse_text()
            elif self.get().type == TK.Space:
                self.discard()  # Discard space at the start of the line
            elif self.get().type == TK.LineFeed:
                return
            else:
                self.error(TK.Null)

        elif self.state[-1] == MD.State.List:
            if self.get().type == TK.SquareBracketOpen:
                self.parse_reference()
            elif self.get().type == TK.Backtick:
                self.parse_code()
            elif self.get().type == TK.Minus:
                self.parse_list()
            elif self.get().type == TK.Space:
                self.discard()  # Discard spaces at the start of the line
            elif self.get().type in TK.Text:
                self.parse_text()
            else:
                self.error(TK.Null)

        elif self.state[-1] == MD.State.Table:
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

    def parse_heading(self):
        self.state.append(MD.State.Heading)

        heading = Heading(None)
        self.curr.add(heading)
        self.curr = heading

        while self.consume(TK.NumberSign):
            pass

        tokens = self.collect_tokens()
        heading.level = len(tokens)

        while self and self.get().type != TK.LineFeed:
            self.parse_nodes()

        self.curr = heading.parent
        self.state.pop()

    def parse_list(self):
        self.state.append(MD.State.List)

        list_root = List(None)
        self.curr.add(list_root)
        self.curr = list_root

        while self and self.get().type != TK.LineFeed:
            self.parse_list_item()

            self.discard()  # Discard line feed

        self.curr = list_root.parent
        self.state.pop()

    def parse_list_item(self):
        list_item = ListItem(None)
        self.curr.add(list_item)
        self.curr = list_item

        self.discard()  # Discard list start

        while self and self.get().type != TK.LineFeed:
            self.parse_nodes()

        self.curr = list_item.parent
        self.consume_until(TK.LineFeed)

        self.curr = list_item.parent

    def parse_table(self):
        self.state.append(MD.State.Table)

        table = Table(None)
        self.curr.add(table)
        self.curr = table

        while self and self.get().type != TK.LineFeed:
            self.parse_table_row()

            self.discard()  # Discard line feed

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

        self.discard()  # Discard row start

        while self and self.get().type != TK.LineFeed:
            self.parse_table_cell()

            self.discard()  # Discard cell separator or row end

        self.curr = row.parent

    def parse_table_cell(self):
        cell = TableCell(None)
        self.curr.add(cell)
        self.curr = cell

        while self and self.get().type != TK.VerticalBar:
            self.parse_nodes()

        self.curr = cell.parent
