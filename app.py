"""Tiny demo: sum of squares + a faster variant, with a small CLI."""

from __future__ import annotations

import argparse
import time
from typing import Iterable, Sequence


def sum_of_squares(numbers: Iterable[int]) -> int:
    total = 0
    for x in numbers:
        total = total + x * x
    return total


def fast_sum_of_squares(numbers: Iterable[int]) -> int:
    # generator-friendly, single-pass
    return sum(x * x for x in numbers)


def _benchmark(numbers: Sequence[int], repeat: int = 1_000_000) -> None:
    """Run each implementation *repeat* times over *numbers* and print wall time."""
    for fn in (sum_of_squares, fast_sum_of_squares):
        t0 = time.perf_counter()
        for _ in range(repeat):
            fn(numbers)
        dt = time.perf_counter() - t0
        print(f"{fn.__name__}: {dt:.4f}s over {repeat} iters")


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="app.py",
        description="Compute the sum of squares of a list of integers.",
    )
    p.add_argument(
        "numbers",
        nargs="*",
        type=int,
        help="Integers whose squares will be summed (default: demo [1,2,3]).",
    )
    p.add_argument(
        "--slow",
        action="store_true",
        help="Use the explicit-loop implementation instead of the generator one.",
    )
    p.add_argument(
        "--benchmark",
        action="store_true",
        help="Time both implementations over the given numbers (default [1,2,3,4]).",
    )
    return p


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.benchmark:
        # benchmark reuses positional numbers if provided, else falls back to [1,2,3,4]
        nums = args.numbers or [1, 2, 3, 4]
        _benchmark(nums)
        return 0

    numbers = args.numbers if args.numbers else [1, 2, 3]
    fn = sum_of_squares if args.slow else fast_sum_of_squares
    print(fn(numbers))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
