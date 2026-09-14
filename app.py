"""Tiny demo: sum of squares + a faster variant."""

from typing import Iterable


def sum_of_squares(numbers: Iterable[int]) -> int:
    total = 0
    for x in numbers:
        total = total + x * x
    return total


def fast_sum_of_squares(numbers: Iterable[int]) -> int:
    # generator-friendly, single-pass
    return sum(x * x for x in numbers)


if __name__ == "__main__":
    print(sum_of_squares([1, 2, 3]))            # 14
    print(fast_sum_of_squares([1, 2, 3, 4]))    # 30