from stats import get_num_words
from stats import get_char_count

def main():
    path = "books/frankenstein.txt"
    book = get_book_text(path)
    words_count = get_num_words(path)
    char_count = get_char_count(path)
    print(words_count)
    print(char_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
