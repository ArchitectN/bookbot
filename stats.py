
def get_num_words(path):
    with open(path) as file:
        content = file.read()
        words = content.split()
        total_words = len(words)
    return f"{total_words} words found in the document"


letter_count = {}

def get_char_count(path):
    with open(path) as file:
        content = file.read()
        words = 