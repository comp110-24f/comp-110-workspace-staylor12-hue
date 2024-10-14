"""Practicing with for loops"""

pets: list[str] = ["Louie", "Bo", "Bear"]

# for p in pets:
# print(f"Good boy, {p}!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for idx in range(0, len(names)):
    # if you're using range, always use "idx"
    print(str(idx) + ": " + names[idx])
