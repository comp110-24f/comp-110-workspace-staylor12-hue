"""Display weather instructions"""


def get_weather_report() -> str:
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()

age: int = 10
age = age + 1
print(age)


x: int = 1
x = x + 1
print(x)
