"""Advent of Code 2024 - Day 2: Red-Nosed Reports.

A report (a list of integer "levels") is *safe* when:
  1. The levels are entirely increasing or entirely decreasing, and
  2. Every pair of adjacent levels differs by between 1 and 3 inclusive.

Part 1 counts the safe reports.
Part 2 adds a "Problem Dampener": a report also counts as safe if it can be
made safe by removing a single level.
"""
import sys

from __future__ import annotations

from pathlib import Path


def parse(text: str) -> list[list[int]]:
    """Parse raw puzzle text into a list of reports (lists of ints)."""
    return [
        [int(n) for n in line.split()]
        for line in text.splitlines()
        if line.strip()
    ]


def is_safe(levels: list[int]) -> bool:
    """Return True if a single report satisfies the safety rules."""
    diffs = [b - a for a, b in zip(levels, levels[1:])]
    increasing = all(1 <= d <= 3 for d in diffs)
    decreasing = all(-3 <= d <= -1 for d in diffs)
    return increasing or decreasing


def is_safe_dampened(levels: list[int]) -> bool:
    """Safe as-is, or safe after removing exactly one level (Part 2)."""
    if is_safe(levels):
        return True
    return any(
        is_safe(levels[:i] + levels[i + 1:])
        for i in range(len(levels))
    )


def part1(reports: list[list[int]]) -> int:
    return sum(is_safe(report) for report in reports)


def part2(reports: list[list[int]]) -> int:
    return sum(is_safe_dampened(report) for report in reports)


def main() -> None:
    input_path = Path(__file__).resolve().parent.parent / "input.txt"
    
    # Check if the file exists before trying to read it
    if not input_path.exists():
        print("❌ Error: input.txt not found!")
        print("Please download your unique puzzle input from Advent of Code")
        print("and save it as 'input.txt' in the main project folder.")
        sys.exit(1) # Exit the script with an error code

    reports = parse(input_path.read_text())
    print(f"Part 1: {part1(reports)}")
    print(f"Part 2: {part2(reports)}")

if __name__ == "__main__":
    main()
