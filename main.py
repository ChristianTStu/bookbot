from stats import get_num_words, get_num_char


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(book_text)
    char_count = get_num_char(book_text)
    print(f"{word_count} words found in the document")
    print(char_count)


main()