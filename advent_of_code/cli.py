"""CLI"""
import sys

import click

from advent_of_code import tools


@click.command("aoc")
@click.argument("year", type=click.IntRange(min=2015, max=2019))
@click.argument("day", type=click.IntRange(min=1, max=25))
@click.option(
    "--file", "-f", type=click.File(lazy=True), required=True,
    help="Path to file from which to read this.")
def aoc(year, day, file=None):
    """Command line tool"""
    print(year, day)
    func_to_call = tools.get_func(year, day)
    if file is None:
        for _ in range(2):
            next(sys.stdin)
        print(sys.stdin.seekable())
        inp = sys.stdin  # ignore the first two inputs.
        output = func_to_call(inp)
    else:
        output = func_to_call(file)
    print(output)
