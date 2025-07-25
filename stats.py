# Contains function definitions for analysis of book text

# Function get_num_words
def get_book_text(book):
    with open(book) as b:
        file_contents = b.read()
    return file_contents

# Function get_num_words
def get_num_words(book):
    book_words = book.split()
    return len(book_words)

# Function get_num_characters
# Argument(s): variable containing book text
# Logic: Convert all chars to lower case and then create a count of characters in the text ('x' : nnnnn, 'y', nnnnn)
# Return(s): dictionary of character count pairs
def get_num_characters(book):

    book_text_characters = list(book.lower())

    book_char_dict = []

    for character in book_text_characters:

        # Check if character already exists in list of dictionaries
        found = False
        for entry in book_char_dict:
            if entry["key"] == character:
                entry["value"] += 1
                found = True
                break

        # If character not found and is alphanumeric, add it with value 1
        if not found and character.isalpha():
            book_char_dict.append({"key": character, "value": 1})

    return book_char_dict

# Function sort_on
# Argument(s):
# Logic:
# Return(s):
def sort_on(items):
    return items["value"]

def print_report(book, num_words, num_characters):

    # Header
    print("============ BOOKBOT ============")

    # Book Path
    print(f"Analyzing book found at {book}...")

    # Word Count
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Character count
    print("--------- Character Count -------")
    for character in num_characters:
        print(f"{character["key"]}: {character["value"]}")

    # Report End
    print("============= END ===============")

    return