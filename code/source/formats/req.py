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


class REQ(Document, Parser):
    def __init__(self, filepath: Path, tokens: list[Token]):
        super().__init__(filepath=filepath, tokens=tokens)

        self.curr = self

    @staticmethod
    def read(filename: str = None, filepath: Path = None, file: FileIO = None, stream: StringIO = None):

        lexer = Lexer(filename, filepath, file, stream)
        tokens : list[Token] = lexer.tokenize()

        req = REQ(filepath, tokens)

        while req:
            if req.get().type in TK.Whitespaces:
                req.discard() # Discard whitespaces at the start of a line

            # Comment
            elif req.get().type == TK.Minus:
                req.consume_until(TK.LineFeed)
                
                req.add(Comment(req.collect_tokens()))

                req.discard() # \n

            # Begin Block
            elif req.get().type == TK.CurlyBracketOpen:
                req.discard() # {

                req.consume_until(TK.LineFeed)

                req.discard() # \n

            # End Block
            elif req.get().type == TK.CurlyBracketClose:
                req.discard() # }

                req.consume_until(TK.LineFeed)

                req.discard() # \n
            
            # Value
            else:
                req.consume_until(TK.LineFeed)

                req.add(Value(req.collect_tokens()))

                req.discard() # \n

        return req


if __name__ == '__main__':
    if len(sys.argv) == 2:
        req = REQ.read(filename=sys.argv[1])
    elif len(sys.argv) > 2:
        req = REQ.read(stream=sys.stdin)
    else:
        sys.exit(1)
    
    req.print()