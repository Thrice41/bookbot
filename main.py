#
#
#
#

# Sys module
import sys
# Functions from /bookbot/stats.py
from stats import get_book_text, get_num_words, get_num_characters, sort_on, print_report

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():

    book = sys.argv[1]

    book_text = get_book_text(book)

    book_words = get_num_words(book_text)

    book_text_characters = get_num_characters(book_text)

    book_text_characters.sort(reverse=True, key=sort_on)

    print_report(book, book_words, book_text_characters)

    return


main()