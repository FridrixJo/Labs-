import unittest
from parser import Parser


class TestCountSentences(unittest.TestCase):
    def test_empty_text(self):
        expected = 0
        text = ''
        actual = Parser(text).count_sentences()
        self.assertEqual(actual, expected, 'empty text test: result is not {expect}')
        actual = Parser(text).count_non_declarative_sentences()
        self.assertEqual(actual, expected, 'empty text test: result is not {expect}')

    def test_simple_text(self):
        text = 'Hello, how are you. I am fine.'
        expected = 2
        actual = Parser(text).count_sentences()
        self.assertEqual(actual, expected, f'text test: result is not {expected}')


class TestCountNoneDeclarativeSentences(unittest.TestCase):
    def test_empty_text(self):
        expected = 0
        text = ''
        actual = Parser(text).count_non_declarative_sentences()
        self.assertEqual(actual, expected, 'empty text test: result is not {expect}')

    def test_simple_text(self):
        text = 'Hello! How are you. I am fine.'
        expected = 3
        actual = Parser(text).count_sentences()
        self.assertEqual(actual, expected, f'text test: result is not {expected}')


class TestAverageWordLenth(unittest.TestCase):
    def test_empty_text(self):
        expected = None
        text = ''
        actual = Parser(text).count_average_length()
        self.assertEqual(actual, expected, 'empty text test: result is not {expect}')

    def test_simple_text(self):
        text = 'Asfkdljlksd 354, fkjhhdfjhjkd  hola  3453d5234  frjfifr 343423, priver gola fojojfr, frifr . Fr!'
        expected = 6.7
        actual = Parser(text).count_average_length()
        self.assertEqual(actual, expected, f'text test: result is not {expected}')

class TestTopKRelatedNGrams(unittest.TestCase):
    def test_empty_text(self):
        expected = []
        text = ''
        actual = Parser(text).top_K_related_N_grams()
        self.assertEqual(actual, expected, 'empty text test: result is not {expect}')

    def test_simple_text(self):
        text = 'Asfkdljlksd 354, fkjhhdfjhjkd  hola  3453d5234  frjfifr 343423, priver gola fojojfr, frifr . Fr!'
        expected = [(('Asfkdljlksd', '354'), 1), (('354', 'fkjhhdfjhjkd'), 1), (('fkjhhdfjhjkd', 'hola'), 1)]

        actual = Parser(text).top_K_related_N_grams(3, 2)
        self.assertEqual(actual, expected, f'text test: result is not {expected}')


if __name__ == '__main__':
    unittest.main()