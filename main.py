from stats import get_num_words
from stats import get_char_count
from stats import transform_list
import sys


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book")

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = get_book_text(sys.argv[1])
        words_count = get_num_words(sys.argv[1])
        char_count = get_char_count(sys.argv[1])
        transform_dict = transform_list(char_count)
        print("----------- Word Count ----------")
        print("Found " + str(words_count) + " total words")
        print("--------- Character Count -------")
        for letters in transform_dict:
            print(str(letters["char"]) + ": " + str(letters["num"]))
        print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

