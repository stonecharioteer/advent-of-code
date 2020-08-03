"""
--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating contest year after
year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on
how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are
at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or
toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents
opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore
refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights,
turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?


"""


from typing import Iterable, Tuple, TextIO


def run(inp: TextIO) -> Tuple[int, int]:
    """Returns lights lit"""
    prefixes = ["turn on", "turn off", "toggle"]
    light_states = list([0]*1000 for _ in range(1000))

    for line in inp:
        line = line.strip()
        if line == "":
            continue
        prefix = [p for p in prefixes if line.startswith(p)][0]
        positions = line[len(prefix)+1:].strip()
        start, end = positions.split("through")
        start_x, start_y = (int(i) for i in start.split(","))
        end_x, end_y = (int(i) for i in end.split(","))

        for ix in range(start_x, end_x):
            for iy in range(start_y, end_y):
                if prefix == "turn on":
                    light_states[ix][iy] = 1
                elif prefix == "turn off":
                    light_states[ix][iy] = 0
                else:
                    light_states[ix][iy] = int(not light_states[ix][iy])
    lights_on = 0
    for row in light_states:
        for col in row:
            lights_on += col

    return (lights_on, None)
