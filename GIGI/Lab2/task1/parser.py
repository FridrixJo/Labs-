import re
from expressions import *

class Parser:
    def __init__(self, text):
        self.text = text

    def count_sentences(self):
        sentences = re.findall(exp_sentences, self.text)
        return len(sentences)

    def count_non_declarative_sentences(self):
        sentences = re.findall(exp_non_dec_sentences, self.text)
        return len(sentences)

    def count_words(self):
        return len(re.findall(exp_all_words, self.text)) - len(re.findall(exp_numbers, self.text))

    def get_all_words(self):
        return re.findall(exp_all_words, self.text)

    def get_words(self):
        return [x for x in self.get_all_words() if x not in self.get_numbers()]

    def get_numbers(self):
        return re.findall(exp_numbers, self.text)

    def count_average_length(self):
        count = 0
        words = self.get_words()
        for word in words:
            count += len(word)

        try:
            return count/len(words)
        except ZeroDivisionError:
            print('Division by zero')
            return None

    def top_K_related_N_grams(self, k: int = 0, n: int = 0):
        exp = r'\W+'
        text = re.sub(exp, ' ', self.text)
        words = text.split()

        ngrams = []

        for i in range(len(words) - n + 1):
            current_ngram = tuple(words[i:i+n])
            ngrams.append(current_ngram)

        counts = {}

        for ngram in ngrams:
            if ngram in counts:
                counts[ngram] += 1
            else:
                counts[ngram] = 1

        sorted_ngrams = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        return sorted_ngrams[0:k]



