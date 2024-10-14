"""Basic sintax and lists"""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor


my_numbers.append(1.5)

# print(my_numbers)

game_points: list[int] = [102, 86, 94]
# print(game_points)

# Subscription Notation/Indexing
last_game: int = game_points[2]

game_points[1] = 72

# print(game_points)

len(game_points)

# Removing an item
game_points.pop(1)
# print(game_points)

# Function name: display
# Parameters: list of integers
# RV: None
# Print every element in the input list
# Call display on game_points


def display(int_list: list[int]) -> None:
    """Display all elements of int_list"""

    index: int = 0

    while index < len(int_list):
        print(int_list: index)
        index += 1


display(int_list=game_points)


print(display(game_points))

grocery_list: list[str] = ["bananas", "milk", "eggs"]

#grocery_list.append("bananas")
print(grocery_list)
