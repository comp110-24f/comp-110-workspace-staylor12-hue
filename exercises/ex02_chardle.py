"""EX02 - Chardle - A cute step towards Wordle"""

__author__ = "730578660"


def input_word() -> str:
    """Asking for a 5-character word"""
    five_char: str = input("Enter a 5-character word: ")
    # Originally had this in two separate lines of code, then combined
    if len(five_char) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
        # printing out an error message, if the word is right, it will move on and print the word
        # I simplified this code, before I used < or > to determine if the length was wrong.
    else:
        return five_char


def input_letter() -> str:
    one_char: str = input("Enter a single character: ")

    if len(one_char) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        return one_char
    # returning or exiting the function


def contains_char(word: str, letter: str) -> None:
    count: int = 0
    # This chain of if statements counts and tells the user when the letter
    # found in the word.
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    elif count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)

    return None


def main() -> None:
    # This main function puts the functions together in one place to make it all easy to call
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
