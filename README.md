# Advent of Code 2024 — Day 2: Red-Nosed Reports

Solution for [AoC 2024 Day 2](https://adventofcode.com/2024/day/2) in Python.

## The puzzle

Each line of input is a **report** — a list of integer **levels**. A report is
**safe** when both of these hold:

1. The levels are either all increasing or all decreasing.
2. Every pair of adjacent levels differs by between **1 and 3** inclusive.

- **Part 1** — count how many reports are safe.
- **Part 2** — the *Problem Dampener*: a report is also safe if removing a
  single level makes it safe. Count how many reports are safe under this rule.

## Project layout

```
aoc-2024-day02/
├── input.txt              # puzzle input
├── src/
│   └── solution.py        # both parts
├── tests/
│   └── test_solution.py   # tests against the AoC example
├── .gitignore
└── README.md
```

## Usage

Run the solution (reads `input.txt` from the project root):

```bash
python src/solution.py
```

Run the tests:

```bash
python tests/test_solution.py
# or, if you use pytest:
pytest
```

## My answers

| Part | Answer |
|------|--------|
| 1    | 472    |
| 2    | 520    |

> Note: AoC generates a unique input per account, so these answers correspond
> to the `input.txt` in this repo. Swap in your own input to get yours.

## How it works

`is_safe` computes the consecutive differences once, then checks whether they
are all in `[1, 3]` (increasing) or all in `[-3, -1]` (decreasing).

`is_safe_dampened` returns early if the report is already safe; otherwise it
tries removing each level in turn and re-checks. With reports this short, the
brute-force `O(n²)` dampener is plenty fast.
