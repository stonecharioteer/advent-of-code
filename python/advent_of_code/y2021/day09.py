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

--- Part Two ---

Next, you need to find the largest basins so you know what areas are most
important to avoid.

A basin is all locations that eventually flow downward to a single low point.
Therefore, every low point has a basin, although some basins are very small.
Locations of height 9 do not count as being in any basin, and all other
locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the
low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678

The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678

The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

Find the three largest basins and multiply their sizes together. In the above
example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?
"""
from queue import Queue
from typing import Tuple, TextIO


def run(inp: TextIO) -> Tuple[int, int]:
    """Solution for 2021 day 9"""
    data = inp.read().splitlines()
    return smoke_basin(data)


def smoke_basin(data):
    """Solves the problem"""
    part_1 = 0
    part_2 = 0
    # create a matrix with the data
    matrix = [[int(x) for x in line] for line in data]
    mins = []
    for ix, line in enumerate(matrix):
        if ix == 0:
            prev_line = None
        else:
            prev_line = matrix[ix-1]

        if ix == len(matrix) - 1:
            next_line = None
        else:
            next_line = matrix[ix+1]
        for iy, val in enumerate(line):
            if iy == 0:
                left = None
            else:
                left = line[iy-1]
            if iy == len(line) - 1:
                right = None
            else:
                right = line[iy+1]
            if prev_line == None:
                top = None
            else:
                top = prev_line[iy]
            if next_line is None:
                bottom = None
            else:
                bottom = next_line[iy]
            current = val
            neighbors = [x for x in [top, right, bottom, left] if x is not None]
            if all([current < neighbor for neighbor in neighbors]):
                mins.append(current)
                part_1 += (1 + current)

    # part 2 is a graph traversal problem,
    # breadth first traversal
    # read up here: https://www.redblobgames.com/pathfinding/a-star/introduction.html

    # create an empty array in which to hold the sums of basin depths
    # we encounter
    basins = []
    visited = set()
    # first, iterate through each row.

    for row_number, row in enumerate(matrix):
        for col_number, value in enumerate(row):
            # now, get the `frontier` (see the above link)
            frontier = Queue()
            if value == 9:
                continue
            basin_points = set()
            # add the current position to the `frontier`
            if (row_number, col_number) in visited:
                continue
            frontier.put((row_number, col_number))
            # as long as the `frontier` is not empty
            while not frontier.empty():
                current = frontier.get()
                basin_points.add(current)
                visited.add(current)
                # calculate all the next neighbors for
                # this current
                neighbors = get_neighbors(matrix, current)
                for pos in neighbors:
                    r, c = pos
                    # if this next item is a value *lower* than the
                    # current value
                    neighbor_value = matrix[r][c]
                    if neighbor_value != 9 and pos not in visited:
                        frontier.put(pos)
                        basin_points.add(pos)
            basin_size = len(basin_points)
            basins.append(basin_size)
    basins.sort()
    three_largest_basins = basins[-3:]
    part_2 = three_largest_basins[0]*three_largest_basins[1]*three_largest_basins[2]
    return part_1, part_2

def get_neighbors(matrix, position):
    """Given an m x n matrix and a position row x col, this returns a list of
    positions of the neighbors, note that this has no parameters regarding the
    filtering of a matrix."""
    row, col = position
    rows = len(matrix)
    cols = len(matrix[0])
    neighbors = set()
    # calculate the neighbors for a given point in the 2D space
    if row-1 != -1:
        neighbors.add((row-1, col))
    if col-1 != -1:
        neighbors.add((row, col-1))
    if row+1 <= rows-1:
        neighbors.add((row+1, col))
    if col+1 <= cols-1:
        neighbors.add((row, col+1))
    return neighbors
