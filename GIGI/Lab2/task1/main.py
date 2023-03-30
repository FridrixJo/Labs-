from parser import Parser

with open('file.txt', 'r') as file:
    text = file.read()

parser = Parser(text)
print(parser.count_sentences())
print(parser.count_non_declarative_sentences())
print(parser.count_words())
print(parser.get_all_words())
print(parser.get_numbers())
print(parser.get_words())
print(parser.count_average_length())
print(parser.top_K_related_N_grams(3, 2))
