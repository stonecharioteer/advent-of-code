from typing import Callable, TextIO
import importlib
import os
import pathlib
import jinja2


def get_func(year: int, day: int) -> Callable[[TextIO], int]:
    try:
        module = importlib.import_module(f"advent_of_code.y{year}.day{day:02d}")
    except ModuleNotFoundError as e:
        raise NotImplementedError(f"No solution implemented yet for {year} x {day}!") from e
    return module.run


def create_file(year: int, day: int):
    """Creates a templatized file for AoC"""
    try:
        current_directory = pathlib.Path(os.path.dirname(__file__))
    except NameError:
        current_directory = pathlib.Path() / "advent_of_code"
    file_path = current_directory / f"y{year}" / f"day{day:02}.py"
    folder_path = file_path.parent
    folder_path.mkdir(parents=True, exist_ok=True) 
    if file_path.exists():
        raise FileExistsError(f"File `{file_path}`already exists, unable to create from template!")
    else:
        template_file = current_directory / "template.py"
        with open(template_file) as f:
            template_contents = f.read()
            template = jinja2.Template(template_contents)
        
        with open(file_path, "w") as f:
            f.write(template.render(year=year, day=day))
        return file_path.absolute()
