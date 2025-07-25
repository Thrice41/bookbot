from stats import get_num_words, get_num_characters, sort_on

def main():

    book = "./books/frankenstein.txt"

    book_text = get_book_text(book)

    print(f"{get_num_words(book_text)} words found in the document")

    book_text_characters = get_num_characters(book_text)

    book_text_characters.sort(reverse=True, key=sort_on)

    for character in book_text_characters:
        print(f"'{character["key"]}': {character["value"]}")


    return

def get_book_text(book):
    with open(book) as b:
        file_contents = b.read()
    return file_contents

main()