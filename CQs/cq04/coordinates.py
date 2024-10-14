"""Coordinates for CQ04"""

__author__ = "730578660"


def get_coords(xs: str, ys: str) -> None:
    idx1: int = 0

    while len(xs) > idx1:
        idx2: int = 0
        while len(ys) > idx2:
            print("(" + xs[idx1] + "," + ys[idx2] + ")")
            idx2 += 1
        idx1 += 1


get_coords("12", "34")
