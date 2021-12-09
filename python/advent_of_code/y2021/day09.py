"""--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active;
small hydrothermal vents release smoke into the caves that slowly settles like
rain.

If you can model how the smoke flows through the caves, you might be able to
avoid it and be that much safer. The submarine generates a heightmap of the
floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the
following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678

Each number corresponds to the height of a particular location, where 9 is the
highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than
any of its adjacent locations. Most locations have four adjacent locations (up,
down, left, and right); locations on the edge or corner of the map have three
or two adjacent locations, respectively. (Diagonal locations do not count
as adjacent.)

In the above example, there are four low points, all highlighted: two are in
the first row (a 1 and a 0), one is in the third row (a 5), and one is in the
bottom row (also a 5). All other locations on the heightmap have some lower
adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the
risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of
all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk
levels of all low points on your heightmap?

{{problem_statement_2 | default("Paste Problem Part 2 here")}}
"""
from typing import Tuple, Iterable


def run(inp: Iterable) -> Tuple[int, int]:
    """Solution for 2021 day 9"""
    data = inp.read().splitlines()
    return smoke_basin(data)


def smoke_basin(data):
    """Solves the problem"""
    part_1 = 0
    part_2 = 0
    mins = []
    for ix, line in enumerate(data):
        if ix == 0:
            prev_line = None
        else:
            prev_line = data[ix-1]

        if ix == len(data) - 1:
            next_line = None
        else:
            next_line = data[ix+1]
        for iy, val in enumerate(line):
            if iy == 0:
                left = None
            else:
                left = int(line[iy-1])
            if iy == len(line) - 1:
                right = None
            else:
                right = int( line[iy+1] )
            if prev_line == None:
                top = None
            else:
                top = int(prev_line[iy])
            if next_line is None:
                bottom = None
            else:
                bottom = int(next_line[iy])
            current = int(val)
            neighbors = [x for x in [top, right, bottom, left] if x is not None]
            if all([current < neighbor for neighbor in neighbors]):
                mins.append(current)
                part_1 += (1 + current)
    return part_1, part_2

