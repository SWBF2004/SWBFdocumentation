import sys
from pathlib import Path
from io import FileIO, StringIO
from util.lexer import Lexer
from util.parser import Parser
from util.nodes import Node, Document, LexicalNode
from util.token import TK, Token


class Comment(LexicalNode):
    def __init__(self, tokens: list[Token], parent: Node = None):
        super().__init__(tokens, parent)


class Key(LexicalNode):
    def __init__(self, tokens: list[Token], parent: Node = None):
        super().__init__(tokens, parent)

        self.key : str = self.raw().strip()

class Value(LexicalNode):
    def __init__(self, tokens: list[Token], parent: Node = None):
        super().__init__(tokens, parent)

        self.value : str = self.raw().strip()


class Section(LexicalNode):
    def __init__(self, tokens: list[Token], parent: Node = None):
        super().__init__(tokens, parent)

        self.name : str = self.raw().strip()


class ODF(Document, Parser):
    def __init__(self, filepath: Path, tokens: list[Token]):
        super().__init__(filepath=filepath, tokens=tokens)

        self.curr = self

    @staticmethod
    def read(filename: str = None, filepath: Path = None, file: FileIO = None, stream: StringIO = None) -> Document:

        lexer = Lexer(filename, filepath, file, stream)
        tokens : list[Token] = lexer.tokenize()

        odf = ODF(filepath, tokens)

        while odf:
            if odf.get().type in TK.Whitespaces:
                odf.discard() # Discard whitespaces at the start of a line

            # Comment
            elif odf.get().type == TK.Slash:
                odf.consume_until(TK.LineFeed)
                
                odf.add(Comment(odf.collect_tokens()))

                odf.discard() # \n

            # Section
            elif odf.get().type == TK.SquareBracketOpen:
                odf.discard() # [

                odf.consume_until(TK.SquareBracketClose)

                if odf.curr != odf:
                    odf.curr = odf.curr.parent

                section = Section(odf.collect_tokens())
                odf.curr = section
                odf.add(section)

                odf.discard() # ]

            # Key value pair
            else:
                while odf.consume(TK.Word):
                    pass

                odf.add(Key(odf.collect_tokens()))

                while odf.consume_any([TK.EqualSign] + TK.Whitespaces):
                    pass

                odf.collect_tokens() # Discard whitespaces and '=' between key and value 

                odf.consume_until(TK.LineFeed)

                odf.add(Value(odf.collect_tokens()))

                odf.discard() # \n

        return odf


if __name__ == '__main__':
    if len(sys.argv) == 2:
        odf = ODF.read(filename=sys.argv[1])
    elif len(sys.argv) > 2:
        odf = ODF.read(stream=sys.stdin)
    else:
        sys.exit(1)
    
    odf.print()