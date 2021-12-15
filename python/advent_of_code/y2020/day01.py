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

--- Part Two ---

The Elves in accounting are thankful for your help; one of them even
offers you a starfish coin they had left over from a past vacation. They
offer you a second one if you can find three numbers in your expense
report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are
979, 366, and 675. Multiplying them together produces the answer,
241861950.

In your expense report, what is the product of the three entries that sum
to 2020?
"""
from typing import Tuple, TextIO


def run(inp: TextIO) -> Tuple[int, int]:
    """Solution for 2020 day 1"""
    return report_repair(inp)


def two_sum(data, required_sum):
    """Given a list and a required sum, returns 2 items which could form the
    required sum"""
    sorted_data = sorted(data)
    complements = {}
    for value in sorted_data:
        complements[value] = required_sum - value
    for value in sorted_data:
        if complements.get(required_sum - value) is not None:
            return (value, complements[value])


def report_repair(data) -> Tuple[int, int]:
    """Calculates expense report"""
    required_sum = 2020
    data = [int(x) for x in data]
    sorted_data = sorted(data)
    two_sum_value = two_sum(sorted_data, required_sum)
    assert two_sum_value is not None
    part_1 = two_sum_value[0] * two_sum_value[1]
    part_2 = None
    for ix, value in enumerate(sorted_data):
        if ix > 0 and ix < len(sorted_data) - 1:
            complement_value = 2020 - value
            two_sum_value = two_sum(sorted_data[:ix] + sorted_data[ix+1:], complement_value)
            if two_sum_value is not None:
                part_2 = value * two_sum_value[0] * two_sum_value[1]
                break
    return (part_1, part_2)


def report_repair_itertools(data) -> Tuple[int, int]:
    """Calculates expense report using itertools.combinations"""
    from itertools import combinations
    required_sum = 2020
    data = [int(x) for x in data]

    def prod(l):
        """Returns the product of all items in a list"""
        product = 1
        if 0 in l:
            # failsafe to save time, naturally
            return 0
        for item in l:
            product *= item
        return product
    
    part_1 = prod([item for item in combinations(data, 2) if sum(item) == required_sum][0])
    part_2 = prod([item for item in combinations(data, 3) if sum(item) == required_sum][0])
    return part_1, part_2


