"""CLI"""
import sys
import datetime
import click

from advent_of_code import tools

today = datetime.date.today()

if today.month < 12:
    MAX_YEAR = today.year - 1
else:
    MAX_YEAR = today.year

@click.group()
def aoc():
    """Advent of Code CLI"""
    pass

@aoc.command("solve")
@click.argument("year", type=click.IntRange(min=2015, max=MAX_YEAR))
@click.argument("day", type=click.IntRange(min=1, max=25))
@click.option(
    "--file", "-f", type=click.File(lazy=True), required=True,
    help="Path to file from which to read this.")
def solve(year, day, file=None):
    """Runs the appropriate solution for the given year and day."""
    func_to_call = tools.get_func(year, day)
    if file is None:
        for _ in range(2):
            next(sys.stdin)
        inp = sys.stdin  # ignore the first two inputs.
        output = func_to_call(inp)
    else:
        output = func_to_call(file)
    print(output)


@aoc.command("create")
@click.argument("year", type=click.IntRange(min=2015, max=MAX_YEAR))
@click.argument("day", type=click.IntRange(min=1, max=25))
def create(year, day):
    """Creates a new templatized solution file"""
    path = tools.create_file(year, day)
    print(f"Created a new solution at {path}")
