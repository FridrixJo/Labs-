import unittest
from parser import Parser

class TestParser(unittest.TestCase):
    def test_empty_text(self):
        expected = 0
        text = ''
        actual = Parser(text).count_sentences()
        self.assertEqual(actual, expected, )