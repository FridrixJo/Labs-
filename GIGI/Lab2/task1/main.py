from parser import Parser


def main():
    with open('file.txt', 'r') as file:
        text = file.read()
    parser = Parser(text)

    print("count sentences:", parser.count_sentences())
    print("count non declarative", parser.count_non_declarative_sentences())
    print("count words", parser.count_words())
    print("count numbers", parser.get_numbers())
    print("count words", parser.get_words())
    print("count averange length", parser.count_average_length())
    print("top K related N grams", parser.top_K_related_N_grams(3, 2))


if __name__ == '__main__':
    main()
