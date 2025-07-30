from stats import get_num_words

def main():
    path = "books/frankenstein.txt"
    book = get_book_text(path)
    words_count = get_num_words(path)
    print(words_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
