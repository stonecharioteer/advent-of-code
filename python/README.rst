==========================
Advent of Code : Python
==========================

This folder contains the python solutions.

---------------------------
Adding a New Year
---------------------------

Create a folder titled: ``yYYYY`` where ``YYYY`` is the year inside the
``advent_of_code`` folder. Make sure you have an ``__init__.py`` file within
this folder.

Adding a New Day
==================

To add the solution for a new day, create ``dayXX.py`` in the respective
`yyYYYY` folder, where ``XX`` is the day number. AoC days range from 01-25.
Within this file you may declare any number of functions but *one* function
needs to be named ``run``, which returns a ``Tuple[int, int]``, signifying the
solution(s). The first item returned is the first solution, while the second
item returned is the second half of the solution.

Make sure that you copy the problem statement into the docstring for the day.

