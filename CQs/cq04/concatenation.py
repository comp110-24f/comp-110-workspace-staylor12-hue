"""Concatenation for CQ04"""

__author__ = "730578660"


def concat(first: str, second: str) -> str:
    return first + second


word1: str = "happy"
word2: str = "tuesday"


def main() -> None:
    print(concat(word1, word2))


if __name__ == "__main__":
    main()
