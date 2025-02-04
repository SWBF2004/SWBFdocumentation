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


class Block(LexicalNode):
    def __init__(self, tokens: list[Token], parent: Node = None):
        LexicalNode.__init__(self, tokens, parent)

        self.header: str = self.raw().replace('(', '').replace(')', '').strip()

        if self.header not in SKY.Headers:
            logger.warning(f'Block header "{self.header}" is not known.')


class Function(LexicalNode):
    def __init__(self, tokens: list[Token], parent: Node = None):
        LexicalNode.__init__(self, tokens, parent)

        function = self.raw().strip().replace(')', '').replace('(', ',').split(',')

        self.name: str = function[0]
        self.arguments: list[str] = function[1:]

        if self.name not in SKY.Functions:
            logger.warning(f'Function name "{self.name}" is not known.')


class SKY(Document, Parser):
    Headers = [
        'FlatInfo',
        'DomeInfo',
        'DomeModel',
        'LowResTerrain',
        'SkyInfo',
        'SkyObject',
        'SunInfo',
    ]

    Functions = [
        'Ambient',
        'AmbientColor',
        'Angle',
        'BackAngle',
        'BackColor',
        'BackDegree',
        'BottomDirectionalAmbientColor',
        'CharacterAmbientColor',
        'Color',
        'Degree',
        'DetailTexture',
        'DetailTextureScale',
        'Enable',
        'FarSceneRange',
        'Filter',
        'FogColor',
        'FogFar',
        'FogNear',
        'FogRamp',
        'FogRange',
        'Geometry',
        'Height',
        'Intensity',
        'MaxDistance',
        'Modulate',
        'MovementScale',
        'NearSceneRange',
        'ObjectVisibility',
        'Offset',
        'PatchResolution',
        'ShadowColor',
        'Softness',
        'SoftnessParam',
        'TerrainColorDarkening',
        'Texture',
        'TextureSpeed',
        'Threshold',
        'TileSize',
        'TopDirectionalAmbientColor',
        'VehicleAmbientColor'
    ]

    def __init__(self, filepath: Path, tokens: list[Token]):
        Document.__init__(self, filepath=filepath)
        Parser.__init__(self, filepath=filepath, tokens=tokens)

        self.curr = self

    @staticmethod
    def read(filename: str = None, filepath: Path = None, file: FileIO = None, stream: StringIO = None):

        lexer = Lexer(filename, filepath, file, stream)
        tokens: list[Token] = lexer.tokenize()

        sky = SKY(filepath, tokens)

        logger.debug(f'Process {filepath}')

        identifier : str = ''

        while sky:
            if sky.get().type in TK.Whitespaces:
                sky.discard()  # Discard whitespaces

            # Comment
            elif sky.get().type == TK.Minus:
                sky.consume_strict(TK.Minus)

                sky.consume_until(TK.LineFeed)

                sky.curr.add(Comment(sky.collect_tokens()))

                sky.discard()  # \n

            # Comment
            elif sky.get().type == TK.Slash:
                sky.consume_strict(TK.Slash)

                sky.consume_until(TK.LineFeed)

                sky.curr.add(Comment(sky.collect_tokens()))

                sky.discard()  # \n

            # Begin Block
            elif sky.get().type == TK.CurlyBracketOpen:
                sky.discard()  # {

            # End Block
            elif sky.get().type == TK.CurlyBracketClose:
                sky.discard()  # }

                sky.curr = sky.curr.parent

            # Header or Function
            elif sky.get().type == TK.Word:

                # We assume that the sky format can't have nested blocks.

                if isinstance(sky.curr, SKY):
                    sky.consume_until(TK.ParanthesisClose)
                    sky.next()

                    block = Block(sky.collect_tokens())
                    sky.curr.add(block)
                    sky.curr = block

                else:
                    sky.consume_until(TK.Semicolon)
                    sky.next()

                    sky.curr.add(Function(sky.collect_tokens()))

            # Either skip or thow error
            else:
                logger.warning(f'Unrecognized token "{sky.get()} ({sky.tokens()})".')
                sky.discard()
                # sky.error(TK.Null)

        return sky


if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = Path(sys.argv[1])
        if path.is_file():
            sky = SKY.read(filepath=path)
            sky.print()
        else:
            for file in path.rglob('*.sky'):
                sky = SKY.read(filepath=file)

    elif len(sys.argv) > 2:
        sky = SKY.read(stream=sys.stdin)
    else:
        sys.exit(1)

    # TODO: Global exit code
    sys.exit(0)
