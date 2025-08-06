
def get_num_words(path):
    with open(path) as file:
        content = file.read()
        words = content.split()
        total_words = len(words)
    return total_words


def sort_high(path):
    return path["num"]

def get_char_count(path):
    letter_count = {}
    with open(path) as file:
        content = file.read()
        content_lower = content.lower()
        char = list(content_lower)
        for item in char:
            if item.isalpha():
                if item not in letter_count:
                    letter_count[item] = 1
                else:
                    letter_count[item] += 1
    return letter_count

def transform_list(char_count):
    letter_count_dict = []
    for items in char_count:
        letter_count_dict.append({"char": items, "num": char_count[items]})
    letter_count_dict.sort(reverse=True, key=sort_high)
    return letter_count_dict




        
