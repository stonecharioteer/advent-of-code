==========================
Advent of Code : Python
==========================

.. sections:: Sections

This folder contains the python solutions.

-------------------------
Local Setup
-------------------------

I use `poetry` to manage my virtual environment, so head over to
[https://python-poetry.org](https://python-poetry.org/) to get
the CLI and create a shell with:

.. code-block:: bash

    poetry shell
    poetry install

I recommend Python > 3.9.

Using the CLI
====================

After installation, you can use the CLI:

.. code-block:: bash

    ./aoc.py --help
    ./aoc.py solve 2021 1 ../inputs/2021/day01.txt
    ./aoc.py create 2021 3

The ``create`` command makes use of ``template.py``, which you can modify to
suite your purposes.

Manual Operation
======================

If you want to do things the manual (*sic* the **hard** way), then you can
follow the below instructions.

Adding a New Year
---------------------------

Create a folder titled: ``yYYYY`` where ``YYYY`` is the year inside the
``advent_of_code`` folder. Make sure you have an ``__init__.py`` file within
this folder.

Adding a New Day
---------------------------

To add the solution for a new day, create ``dayXX.py`` in the respective
`yyYYYY` folder, where ``XX`` is the day number. AoC days range from 01-25.
Within this file you may declare any number of functions but *one* function
needs to be named ``run``, which returns a ``Tuple[int, int]``, signifying the
solution(s). The first item returned is the first solution, while the second
item returned is the second half of the solution.

Make sure that you copy the problem statement into the docstring for the day.

Testing
========================

I'm trying to write tests to check for the "sample" problem that's given
with the problem description. I've used ``pytest`` for this.

You can run the tests using the following commands:


.. code-block:: bash

    pytest # this will run tests for all years
    pytest -k 2021 # this will run all tests for 2021
    pytest -k 2021_day04 # this will run the test for 2021 day 4

