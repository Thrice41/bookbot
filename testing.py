book_text_characters = list("attaboy billy red beard!")
book_char_dict = []  # Start with an empty list of dictionaries

for character in book_text_characters:
    # Check if character already exists in list of dictionaries
    found = False
    for entry in book_char_dict:
        if entry["key"] == character:
            entry["value"] += 1
            found = True
            break

    # If character not found, add it with value 1
    if not found:
        book_char_dict.append({"key": character, "value": 1})

print(book_char_dict)
