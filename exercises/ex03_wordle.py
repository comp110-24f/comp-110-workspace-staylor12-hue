"""Creating the Wordle game"""

__author__ = "730578660"


def input_guess(secret_word_len: int) -> str:
    """Prompt user to guess word until it is the right length"""
    guess: str = input(f"Enter a {secret_word_len}-character word: ")
    # used f-string templates
    while len(guess) != secret_word_len:
        # inputs new guess if theirs was the wrong length
        guess = input(f"That wasn't {secret_word_len} characters! Try again: ")
        # if len(guess) == secret_word_len:
        #    return guess
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Check if word of any length contains char"""
    assert len(char_guess) == 1
    index: int = 0
    letter_present: bool = False

    while index < len(secret_word) and letter_present is False:
        if char_guess == secret_word[index]:
            letter_present = True
        else:
            index += 1
    return letter_present


# The print statements using contains_char printed the expected results.


def emojified(guess: str, secret_word: str) -> str:
    """Uses yellow, green, or white emojis to express the accuracy of the guess"""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    hint: str = ""
    while index < len(guess):
        # adding yellow, green, or white emojis to "hint", then returning hint
        if guess[index] == secret_word[index]:
            hint += GREEN_BOX
        elif contains_char(secret_word, guess[index]):
            hint += YELLOW_BOX
        else:
            hint += WHITE_BOX
        index += 1
    return hint


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    # define variables to keep track of them
    secret_word: str = secret
    secret_word_len: int = len(secret_word)
    turn: int = 1
    win: bool = False
    while turn <= 6 and win is False:
        # loops through "turns" until they win or lose
        guess: str = ""

        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(secret_word_len)
        print(emojified(guess, secret_word))

        if guess == secret_word:
            win = True
        else:
            win = False
            turn += 1
    if win is True:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
