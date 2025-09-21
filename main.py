import sys
from stats import get_word_count, get_char_count, sort_char_count

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents


def main():
    if len(sys.argv) != 2:
        return sys.exit(1)
    
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)
    words_count = get_word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    char_dictionary = get_char_count(book_text)
    sorted_char_list = sort_char_count(char_dictionary)
    for char in sorted_char_list:
        print(f"{char['char']}: {char['num']}")

main()
