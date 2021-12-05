import textwrap

from advent_of_code.y2021.day03 import binary_diagonistic
from advent_of_code.y2021.day04 import squidgame_bingo_score
from advent_of_code.y2021.day05 import hydrothermal_vent_overlaps


def test_2021_day03():
    """Tests that the simple test case for 2021 day 03 works"""
    data = textwrap.dedent(""" 
            00100
            11110
            10110
            10111
            10101
            01111
            00111
            11100
            10000
            11001
            00010
            01010
    """)
    data = data.strip().split("\n")
    data = [x for x in data]
    result = binary_diagonistic(data)
    assert isinstance(result, tuple)
    assert result[0] == 198, "Part 1 is wrong"
    assert result[1] == 230, "Part 2 is wrong"

def test_2021_day04():
    """Tests that the simple testcase for 2021 day 04 works"""
    data = textwrap.dedent("""
        7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

        22 13 17 11  0
        8  2 23  4 24
        21  9 14 16  7
        6 10  3 18  5
        1 12 20 15 19

        3 15  0  2 22
        9 18 13 17  5
        19  8  7 25 23
        20 11 10 24  4
        14 21 16 12  6

        14 21 17 24  4
        10 16 15  9 19
        18  8 23 26 20
        22 11 13  6  5
        2  0 12  3  7
    """)
    data = data.strip().split("\n")
    result = squidgame_bingo_score(data)
    assert isinstance(result, tuple)
    assert result[0] == 4512, "Part 1 is wrong"
    assert result[1] == 1924, "Part 2 is wrong"

def test_2021_day05():
    """Tests that the simple testcase for 2021 day 05 works"""
    data = textwrap.dedent("""
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
    """)
    data = data.strip.split("\n") 
    result = hydrothermal_vent_overlaps(data)
    assert isinstance(result , tuple)
    assert result[0] == 5, "Part 1 is wrong"
    NotImplementedError("Part 2 is pending")
