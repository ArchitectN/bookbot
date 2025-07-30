
def get_num_words(path):
    with open(path) as file:
        content = file.read()
        words = content.split()
        total_words = len(words)
    return f"{total_words} words found in the document"


def sort(items):
    return items["num"]

def get_char_count(path):
    letter_count = {}
    with open(path) as file:
        content = file.read()
        content_lower = content.lower()
        char = list(content_lower)
        for item in char:
            if item not in letter_count:
                letter_count[item] = 1
            else:
                letter_count[item] += 1
    letter_count.sort(reverse=True, key=sort_on)
    return letter_count