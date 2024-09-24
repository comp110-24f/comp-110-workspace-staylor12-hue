"""Tea Party Exercise 01"""

__author__: str = "730578660"


def main_planner(guests: int) -> None:
    # trying to figure out what I'm doing wrong here, I keep getting errors
    """Calls and produces tea_bags, treats, and cost functions"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # this first print statement works, but everything else doesn't
    # Does not work: print(string("Tea Bags: " + tea_bags(people=guests))) (this does not work)
    #                print("Cost: $" cost)
    #                print("Tea Bags: " + tea_bags(people=guests))
    # I have tried converting the statement to a string, it also says I cannot use a "+"
    # I was unable to print the string and the int on the same line, I'm trying to figure out how to
    # convert both statements to strings so they can sit side by side
    # print("Tea Bags: ")
    # print(tea_bags(people=guests))
    # print("Treats: ")
    # print(treats(people=guests))
    # print("Cost: ")
    # print(cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests)))

    # Looking in lecture slides to find a way to convert an int to a string
    # Yay I found it! Before I was tring to do string(), but the correct function is str()

    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Compute number of tea bags based on number of guests"""
    return people * 2


def treats(people: int) -> int:
    """Number of necessary treats based on number of teas"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """return cost of tea bags and treats"""
    return (tea_count) * 0.5 + 0.75 * (treat_count)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
