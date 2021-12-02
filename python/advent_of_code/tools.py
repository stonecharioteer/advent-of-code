import importlib
from typing import Callable, Iterable


def get_func(year: int, day: int) -> Callable[[Iterable], int]:
    try:
        module = importlib.import_module(f"advent_of_code.y{year}.day{day:02d}")
    except ModuleNotFoundError as e:
        raise NotImplementedError(f"No solution implemented yet for {year} x {day}!") from e
    return module.run
