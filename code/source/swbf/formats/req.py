import re
import sys
from pathlib import Path
from io import FileIO, StringIO
from util.lexer import Lexer
from util.parser import Parser
from util.nodes import Node, Document, LexicalNode
from util.token import TK, Token
from util.logging import get_logger


logger = get_logger(__name__)


class Comment(LexicalNode):
    def __init__(self, tokens: list[Token], parent: Node = None):
        LexicalNode.__init__(self, tokens, parent)

        self.text: str = self.raw().strip()


class Condition(LexicalNode):
    def __init__(self, tokens: list[Token], parent: Node = None):
        LexicalNode.__init__(self, tokens, parent)

        condition = self.raw().strip().split(' ')

        self.name: str = condition[0]
        self.arguments: list[str] = condition[1:]


class Block(LexicalNode):
    def __init__(self, tokens: list[Token], parent: Node = None):
        LexicalNode.__init__(self, tokens, parent)

        self.header: str = self.raw().strip()
        self.type: str = ''

        if self.header not in REQ.Headers:
            logger.warning(f'Block header "{self.header}" is not known.')


class Type(LexicalNode):

    def __init__(self, tokens: list[Token], parent: Node = None):
        LexicalNode.__init__(self, tokens, parent)

        self.type: str = self.raw().strip()

        if self.type not in REQ.Types:
            logger.warning(f'Block type "{self.type}" is not known.')


class Property(LexicalNode):
    RE = re.compile(r'(.*)=(.*)')

    def __init__(self, tokens: list[Token], parent: Node = None):
        LexicalNode.__init__(self, tokens, parent)

        match = re.match(Property.RE, self.raw())

        self.key: str = match.group(1)
        self.value: str = match.group(2)

        if self.key not in REQ.Properties:
            logger.warning(f'Block property "{self.key}" is not known.')


class Value(LexicalNode):
    def __init__(self, tokens: list[Token], parent: Node = None):
        LexicalNode.__init__(self, tokens, parent)

        self.value: str = self.raw().strip()


class REQ(Document, Parser):
    Headers = [
        'REQN',
        'ucft',
    ]

    Properties = [
        'align',
        'platform',
    ]

    Types = [
        'bin',
        'bnk',
        'boundary',
        'config',
        'congraph',
        'class',
        'envfx',
        'loc',
        'lvl',
        'model',
        'path',
        'prop',
        'script',
        'str',
        'terrain',
        'texture',
        'world',
        'zaabin',
        'zafbin',
    ]

    def __init__(self, filepath: Path, tokens: list[Token]):
        Document.__init__(self, filepath=filepath)
        Parser.__init__(self, filepath=filepath, tokens=tokens)

        self.curr = self

    @staticmethod
    def read(filename: str = None, filepath: Path = None, file: FileIO = None, stream: StringIO = None):

        lexer = Lexer(filename, filepath, file, stream)
        tokens: list[Token] = lexer.tokenize()

        req = REQ(filepath, tokens)

        logger.debug(f'Process {filepath}')

        while req:
            if req.get().type in TK.Whitespaces:
                req.discard()  # Discard whitespaces

            # Comment
            elif req.get().type == TK.Minus:
                req.consume_strict(TK.Minus)

                req.consume_until(TK.LineFeed)

                req.curr.add(Comment(req.collect_tokens()))

                req.discard()  # \n

            # Begin Block
            elif req.get().type == TK.CurlyBracketOpen:
                req.discard()  # {

            # End Block
            elif req.get().type == TK.CurlyBracketClose:
                req.discard()  # }

                req.curr = req.curr.parent

            # Type, Property, Value
            elif req.get().type == TK.QuotationMark:
                req.discard()  # "

                req.consume_until_any([TK.EqualSign, TK.QuotationMark])

                if req.get().type == TK.QuotationMark:

                    if isinstance(req.curr, Block) and len(req.curr.children) == 0:
                        req.curr.add(Type(req.collect_tokens()))

                    else:
                        req.curr.add(Value(req.collect_tokens()))

                elif req.get().type == TK.EqualSign:
                    req.consume_until(TK.QuotationMark)
                    req.curr.add(Property(req.collect_tokens()))

                else:
                    req.error()

                req.discard()  # "

            # Header
            elif req.get().type == TK.Word:
                req.consume(TK.Word)

                block = Block(req.collect_tokens())
                req.curr.add(block)
                req.curr = block

            # Condition
            elif req.get().type == TK.NumberSign:
                req.discard()  # #

                # Condition name
                req.consume(TK.Word)
                req.consume_while_any(TK.Whitespaces)

                # Condition parameters
                while req.get().type == TK.Word:
                    req.consume(TK.Word)
                    req.consume_while_any(TK.Whitespaces)
                
                if isinstance(req.curr, Condition): 
                    req.collect_tokens() # Discard end of condition
                    req.curr = req.curr.parent
                else:
                    condition = Condition(req.collect_tokens())
                    req.curr.add(condition)
                    req.curr = condition

            # Either skip or thow error
            else:
                logger.warning(f'Unrecognized token "{req.get()} ({req.tokens()})".')
                req.discard()
                # req.error(TK.Null)

        return req


if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = Path(sys.argv[1])
        if path.is_file():
            req = REQ.read(filepath=path)
            req.print()
        else:
            for file in path.rglob('*.req'):
                req = REQ.read(filepath=file)

    elif len(sys.argv) > 2:
        req = REQ.read(stream=sys.stdin)
    else:
        sys.exit(1)

    # TODO: Global exit code
    sys.exit(0)
