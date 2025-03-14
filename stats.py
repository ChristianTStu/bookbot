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

            