def get_num_words(text):
    return len(text.split())

def get_num_char(text):
    char_count = {}
    for char in text:
        char = char.lower()

        if char in char_count:
            char_count[char] += 1
        elif char not in char_count:
            char_count[char] = 1

    return char_count

def get_sort_dict(char_count):
    char_list = []
    for char, count in char_count.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)

    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list