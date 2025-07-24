def main():
    print(get_book_text("./books/frankenstein.txt"))
    return

def get_book_text(book):
    with open(book) as b:
        file_contents = b.read()
    return file_contents

main()
