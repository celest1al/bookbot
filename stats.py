def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1

    return char_count

def sort_on_num(dict):
    return dict['num']

def sort_char_count(dictionary):
    list = []
    for key, value in dictionary.items():
        if key.isalpha():
            list.append({ "char": key, "num": value })
    return sorted(list, key=sort_on_num, reverse=True)