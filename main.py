from stats import get_num_words, get_num_char, get_sort_dict


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(book_text)
    char_count = get_num_char(book_text)
    sorted_chars = get_sort_dict(char_count)
    
    # Print the report
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")


main()