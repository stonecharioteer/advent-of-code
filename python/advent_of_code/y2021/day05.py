"""-- Day 5: Hydrothermal Venture ---

You come across a field of hydrothermal vents on the ocean floor! These vents
constantly produce large, opaque clouds, so it would be best to avoid them if
possible.

They tend to form in lines; the submarine helpfully produces a list of nearby
lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2
where x1,y1 are the coordinates of one end the line segment and x2,y2 are the
coordinates of the other end. These line segments include the points at both
ends. In other words:

    An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

For now, only consider horizontal and vertical lines: lines where either x1 =
x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the
following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....

In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9.
Each position is shown as the number of lines which cover that point or . if no
line covers that point. The top-left pair of 1s, for example, comes from 2,2 ->
2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9
-> 2,9.

To avoid the most dangerous areas, you need to determine the number of points
where at least two lines overlap. In the above example, this is anywhere in the
diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two
lines overlap?

--- Part Two ---

Unfortunately, considering only horizontal and vertical lines doesn't give you
the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in
your list will only ever be horizontal, vertical, or a diagonal line at exactly
45 degrees. In other words:

    An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
    An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

Considering all lines from the above example would now produce the following
diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....

You still need to determine the number of points where at least two lines
overlap. In the above example, this is still anywhere in the diagram with a 2
or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?

"""
from typing import Tuple, Iterable
import warnings


def run(inp: Iterable) -> Tuple[int, int]:
    """Solution for 2021 day 5"""
    data = inp.read().splitlines()
    result = hydrothermal_vent_overlaps(data)
    return result


def hydrothermal_vent_overlaps(data) -> Tuple[int, int]:
    """Solves for the hydrothermal vent overlap problem"""
    # One way to do this would be to determine all the points in each line,
    # and then loop through all the points on the "floor",
    # but there is no real need to loop through *all* the points.
    # instead, loop only through the points on that are definitely
    # covered by lines.
    from collections import defaultdict
    points = defaultdict(int)
    for item in data:
        start, end = item.strip().split(" -> ")
        x_1, y_1 = start.split(",")
        x_1, y_1 = int(x_1), int(y_1)
        x_2, y_2 = end.split(",")
        x_2, y_2 = int(x_2), int(y_2)
        # we're being asked to consider only the horizontal or vertical lines.
        if x_1 == x_2:
            y_range = range(y_1, y_2 + 1) if y_1 < y_2 else range(y_2, y_1 + 1)
            for y in y_range:
                points[f"{x_1},{y}"] += 1
        elif y_1 == y_2:
            x_range = range(x_1, x_2 + 1) if x_1 < x_2 else range(x_2, x_1 + 1)
            for x in x_range:
                points[f"{x},{y_1}"] += 1
        else:
            # warnings.warn("Ignoring {} because it's not horizontal or vertical.".format(item))
            # The problem statement says that one of these will be equal to the
            # other.
            pass
     
    part_1 = len([x for x in points.keys() if points[x] >= 2])
    # Again, these two loops *can* be merged. But O(N) * 2 = O(N) so it
    # doesn't matter
    ## diagonals
    # lines will only ever be inclined at 45 degrees, so I can just equally
    # increase x and y
    points_2 = defaultdict(int)
    for item in data:
        start ,end = item.strip().split(" -> ")
        x_1, y_1 = start.split(",")
        x_1, y_1 = int(x_1), int(y_1)
        x_2, y_2 = end.split(",")
        x_2, y_2 = int(x_2), int(y_2)
        if x_1 == x_2:
            y_range = range(y_1, y_2 + 1) if y_1 < y_2 else range(y_1, y_2 - 1, -1)
            for y in y_range:
                points_2[f"{x_1},{y}"] += 1
        elif y_1 == y_2:
            x_range = range(x_1, x_2 + 1) if x_1 < x_2 else range(x_1, x_2 - 1, -1)
            for x in x_range:
                points_2[f"{x},{y_1}"] += 1
        else:
            # need to identify points on diagonal lines
            assert abs(x_1 - x_2) == abs(y_1 - y_2), "The line is not at 45 degrees as assumed."
            x_range = range(x_1, x_2 + 1) if x_1 < x_2 else range(x_1, x_2 - 1, -1)
            y_range = range(y_1, y_2 + 1) if y_1 < y_2 else range(y_1, y_2 - 1, -1)
            for x, y in zip(x_range, y_range):
                points_2[f"{x},{y}"] += 1

    part_2 = len([x for x in points_2.keys() if points_2[x] >= 2])

    return (part_1, part_2)
