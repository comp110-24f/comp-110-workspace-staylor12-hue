"""CQ with Conditionals, Local Variables, and User Input"""

__author__ = 730578660


def guess_a_number() -> None:
    x: int = 0
    secret: int = 7
    x = int(input("Guess a number: "))
    print("Your guess was: " + str(x))
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    elif x > secret:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
