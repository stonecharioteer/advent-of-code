"""--- Day 1: Report Repair ---

After saving Christmas five years in a row, you've decided to take a vacation
at a nice resort on a tropical island. Surely, Christmas will go on without
you.

The tropical island has its own currency and is entirely cash-only. The gold
coins used there have a little picture of a starfish; the locals just call them
stars. None of the currency exchanges seem to have heard of them, but somehow,
you'll need to find fifty of these coins by the time you arrive so you can pay
the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each
day in the Advent calendar; the second puzzle is unlocked when you complete the
first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense
report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then
multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying
them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to
2020; what do you get if you multiply them together?

{{problem_statement_2 | default("Paste Problem Part 2 here")}}
"""
from typing import Tuple, Iterable


def run(inp: Iterable) -> Tuple[int, int]:
    """Solution for 2020 day 1"""
    return report_repair(inp)


def report_repair(data) -> Tuple[int, int]:
    """Calculates expense report"""
    required_sum = 2020
    data = [int(x) for x in data]
    left = 0
    right = len(data) - 1
    sorted_data = sorted(data)
    part_1 = None
    counter = 0
    while left < right:
        left_value = sorted_data[left]
        right_value = sorted_data[right]
        if left_value + right_value > required_sum:
            right -= 1
        elif left_value + right_value < required_sum:
            left += 1
        else:
            part_1 = left_value * right_value
            break
        counter += 1
    part_2 = None
    return (part_1, part_2)
