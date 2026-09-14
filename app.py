"""Tiny demo: sum of squares."""


def sum_of_squares(numbers):
    total = 0
    for x in numbers:
        total = total + x * x
    return total


if __name__ == "__main__":
    print(sum_of_squares([1, 2, 3]))  # 14
