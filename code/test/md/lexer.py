from source.md.lexer import Lexer
from unittest import TestCase


class LexerTest(TestCase):
    def test_empty_buffer(self):
        lex = Lexer([])


    def test_simple_buffer(self):
        lex = Lexer('bli kla dub')


    def test_complex_logix(self):
        lex = Lexer(open(__file__, 'r').read())
