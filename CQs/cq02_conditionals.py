"""CQ with Conditionals, Local Variables, and User Input"""

__author__ = 730578660


def guess_a_number() -> None:
    x: int = 0
    secret: int = 7

if __name__ == "__main__":
    guess_a_number()

print(x=input("Guess a number: "))
print("Your guess was " + str(x))

if secret == x:
    print("You got it!")
elif x<secret:
    print("Your guess was too low! The secret number is " + str(x))
else
    print("Your guess was too high! The secret number is " + str(x))



# if __name__ == "__guess__":
#    guess_a_number(x=input("Guess a number: "))
