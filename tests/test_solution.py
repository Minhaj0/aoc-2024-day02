"""Tests for Day 2 using the official AoC example."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from solution import parse, is_safe, is_safe_dampened, part1, part2  # noqa: E402

EXAMPLE = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def test_parse():
    reports = parse(EXAMPLE)
    assert len(reports) == 6
    assert reports[0] == [7, 6, 4, 2, 1]


def test_individual_safety():
    expected = [True, False, False, False, False, True]
    assert [is_safe(r) for r in parse(EXAMPLE)] == expected


def test_part1_example():
    assert part1(parse(EXAMPLE)) == 2


def test_dampened_safety():
    # 1 3 2 4 5 -> safe by removing the 3; 8 6 4 4 1 -> safe by removing a 4.
    expected = [True, False, False, True, True, True]
    assert [is_safe_dampened(r) for r in parse(EXAMPLE)] == expected


def test_part2_example():
    assert part2(parse(EXAMPLE)) == 4


if __name__ == "__main__":
    test_parse()
    test_individual_safety()
    test_part1_example()
    test_dampened_safety()
    test_part2_example()
    print("All tests passed.")
