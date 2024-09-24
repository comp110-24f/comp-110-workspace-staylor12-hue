"""Practice with Conditionals"""


def less_than_10(num: int) -> bool:
    """Tell me if num is < 10"""
    if num < 10:
        print("Small number")
    else:
        print("Big number")
    print("have a nice day")


# less_than_10(num=4)


def should_i_eat(hungry: bool) -> bool:
    """Tells me whether or not to eat based on hunger."""
    if hungry:  # conditional/boolean expressions
        print("Eat some food")  # "then" block
    else:
        print("Do you Comp 110 homework instead.")  # "else" block
    print("I'm proud of you <3")  # either way, be kind to yourself


# print( should_i_eat(hungry=True))  # if I print this, it will print out None bc there is no return value


def check_first_letter(word: str, letter: str) -> str:
    """Check if letter is first character of word."""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="baby", letter="b"))
print(check_first_letter(word="dinosaur", letter="b"))
