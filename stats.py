def count_words(book_contents):
    split_contents = book_contents.split()
    num_words = len(split_contents)
    return num_words

def count_characters(book_contents):
    dict_list = []
    char_dict = {}

    for char in book_contents:
        char = char.lower()
        if char not in char_dict.keys() and char.isalpha():
            char_dict[char] = 1
        elif char.isalpha():
            char_dict[char] += 1

    for key, value in char_dict.items():
        dict = {'char': key,
                 'num':value
                }
        dict_list.append(dict)

    return dict_list

def sort_on(items):
    return items["num"]

def sort_dicts(dict_list):
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list