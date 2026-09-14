from app import fast_sum_of_squares, sum_of_squares


def test_sum_of_squares():
    assert sum_of_squares([1, 2, 3]) == 14


def test_fast_sum_of_squares():
    assert fast_sum_of_squares([1, 2, 3, 4]) == 30
