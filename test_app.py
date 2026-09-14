from app import fast_sum_of_squares, main, sum_of_squares


def test_sum_of_squares():
    assert sum_of_squares([1, 2, 3]) == 14


def test_fast_sum_of_squares():
    assert fast_sum_of_squares([1, 2, 3, 4]) == 30


def test_cli_default():
    assert main([]) == 0  # default branch is exercised, output goes to stdout


def test_cli_explicit_numbers():
    assert main(["5", "6"]) == 0


def test_cli_slow_flag():
    assert main(["--slow", "1", "2", "3"]) == 0


def test_cli_unknown_flag_exits_nonzero():
    import pytest
    with pytest.raises(SystemExit) as exc:
        main(["--nope"])
    assert exc.value.code != 0
