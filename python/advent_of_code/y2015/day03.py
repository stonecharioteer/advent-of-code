"""--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

"""

from typing import Iterable, Tuple
from collections import defaultdict
from itertools import zip_longest


def grouper(iterable: Iterable, n: int, fillvalue: [int, None] = None) -> Iterable:
    """Groups items in a list"""
    args = [iter(iterable)]*n
    return zip_longest(*args, fillvalue=fillvalue)


def run(inp: Iterable) -> Tuple[int, int]:
    """Solution for day 2"""
    # part 1
    positions_solo = defaultdict(int)
    position_solo = [0, 0]
    positions_solo["0x0"] += 1

    ## Part 2
    positions_combo = defaultdict(int)
    santa_position = [0, 0]
    robot_position = [0, 0]
    positions_combo["0x0"] += 1  # for santa
    positions_combo["0x0"] += 1  # for robot

    for line in inp:
        line = line.strip()
        if line == "":
            continue
        for direction in line:
            if direction == ">":
                position_solo[1] += 1
            elif direction == "<":
                position_solo[1] -= 1
            elif direction == "v":
                position_solo[0] += 1
            elif direction == "^":
                position_solo[0] -= 1
            x, y = position_solo
            positions_solo[f"{x}x{y}"] += 1

        # part 2
        for santa, robot in grouper(line, 2):
            if santa == ">":
                santa_position[1] += 1
            elif santa == "<":
                santa_position[1] -= 1
            elif santa == "v":
                santa_position[0] += 1
            elif santa == "^":
                santa_position[0] -= 1
            x, y = santa_position
            positions_combo[f"{x}x{y}"] += 1
            if robot == ">":
                robot_position[1] += 1
            elif robot == "<":
                robot_position[1] -= 1
            elif robot == "v":
                robot_position[0] += 1
            elif robot == "^":
                robot_position[0] -= 1
            x, y = robot_position
            positions_combo[f"{x}x{y}"] += 1

    lucky_solo = [key for key in positions_solo if positions_solo[key] >= 1]
    lucky_solo = len(lucky_solo)

    lucky_combo = [key for key in positions_combo if positions_combo[key]>=1]
    lucky_combo = len(lucky_combo)

    return (lucky_solo, lucky_combo)
