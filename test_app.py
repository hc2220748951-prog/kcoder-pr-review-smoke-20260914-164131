import pytest

from app import fast_sum_of_squares, main, sum_of_squares


def test_sum_of_squares():
    assert sum_of_squares([1, 2, 3]) == 14


def test_fast_sum_of_squares():
    assert fast_sum_of_squares([1, 2, 3, 4]) == 30


def test_cli_default(capsys):
    rc = main([])
    assert rc == 0
    out = capsys.readouterr().out.strip()
    assert out == "14"


def test_cli_explicit_numbers(capsys):
    rc = main(["5", "6"])
    assert rc == 0
    out = capsys.readouterr().out.strip()
    # fast_sum_of_squares([5, 6]) == 25 + 36 == 61
    assert out == "61"


def test_cli_slow_flag(capsys):
    rc = main(["--slow", "1", "2", "3"])
    assert rc == 0
    out = capsys.readouterr().out.strip()
    # sum_of_squares([1, 2, 3]) == 14
    assert out == "14"


def test_cli_unknown_flag_exits_nonzero():
    with pytest.raises(SystemExit) as exc:
        main(["--nope"])
    assert exc.value.code != 0
