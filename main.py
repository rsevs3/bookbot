def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    alphabet = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0}

    lowered_text = text.lower()

    for character in lowered_text:
        if character in alphabet:
            alphabet[character] += 1

    return alphabet

def generate_report(word_count, character_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for i in character_count:
        print(f"The '{i}' character was found {character_count[i]} times")
    print("--- End Report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(count_words(file_contents))        
        # print(count_characters(file_contents))
        generate_report(count_words(file_contents), count_characters(file_contents))

main()
