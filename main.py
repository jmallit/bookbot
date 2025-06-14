import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import (
    get_num_words,
    get_char_count,
    sorted_lists
)
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def printed_report(book_path, count_words, everything_sorted):
    print("============ BOOKBOT ============")
    print("Analyzing book found at", book_path)
    print("----------- Word Count ----------")
    print("Found", count_words, "total words")
    print("--------- Character Count -------")
    for item in everything_sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
def main():
    book_path = sys.argv[1]

    book_contents = get_book_text(book_path)
    count_words = get_num_words(book_contents)
    char_count = get_char_count(book_contents)
    everything_sorted = sorted_lists(char_count)
    printed_report(book_path, count_words, everything_sorted)
main()


