from source.md.iterator import Iterator
from unittest import TestCase


class IteratorTest(TestCase):
    def test_empty_buffer(self):
        it = Iterator([])

        self.assertFalse(it)
        self.assertEqual(it.get(), None)
        self.assertEqual(it.next(), None)
        self.assertEqual(it.prev(), None)

    def test_simple_buffer(self):
        it = Iterator('bli kla dub')

        self.assertTrue(it)
        self.assertEqual(it.get(), 'b')
        self.assertEqual(it.next(), 'l')
        self.assertEqual(it.prev(), 'b')
        self.assertEqual(it.advance(2), 'i')
        self.assertEqual(it.peek(2), 'k')
        self.assertEqual(it.consume('i'), True)
        self.assertEqual(it.consume_any(' '), True)

    def test_complex_logix(self):
        it = Iterator(open(__file__, 'r').read())

        self.assertTrue(it)

        s = ''
        while it:
            if it.get() not in ' \n\r.()[]=\',:\\+_':
                s += it.get()

            it.next()
        
        self.assertFalse(it)
        self.assertEqual(len(set([x.isalnum() for x in s])), 1)
