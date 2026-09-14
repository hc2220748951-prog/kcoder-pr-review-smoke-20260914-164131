"""Tiny demo: sum of squares + a faster variant."""


def sum_of_squares(numbers):
    total = 0
    for x in numbers:
        total = total + x * x
    return total


def fast_sum_of_squares(numbers):
    # generator-friendly, single-pass
    return sum(x * x for x in numbers)


def unsafe_eval(expr):
    # TODO: replace with ast.literal_eval before shipping
    return eval(expr)  # noqa: S307


if __name__ == "__main__":
    print(sum_of_squares([1, 2, 3]))            # 14
    print(fast_sum_of_squares([1, 2, 3, 4]))    # 30
    print(unsafe_eval("1 + 2"))                 # demo only
