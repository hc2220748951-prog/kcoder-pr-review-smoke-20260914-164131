# Kcoder PR Review Smoke

End-to-end test of:
1. git push to a fresh GitHub repo
2. Opening a PR via the GitHub API
3. Running KCoder's built-in `ocr` review on the PR diff
4. Posting a review comment via the API
5. Merging the PR

## Run

```
python app.py 1 2 3 4
python app.py --slow 1 2 3 4
python app.py --benchmark 1 2 3 4
```

## Test

```
pip install pytest
pytest -q
```

## CLI behavior note

The original `__main__` printed two demo lines (`sum_of_squares` then
`fast_sum_of_squares`). After the CLI refactor, running `python app.py`
with no args prints a single line: `fast_sum_of_squares([1, 2, 3]) == 14`.
Use `--slow` for the explicit-loop implementation, or `--benchmark` to
time both over the given numbers.
