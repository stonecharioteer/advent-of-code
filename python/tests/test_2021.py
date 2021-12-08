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
    data = data.strip().split("\n") 
    result = hydrothermal_vent_overlaps(data)
    assert isinstance(result , tuple)
    assert result[0] == 5, "Part 1 is wrong"
    assert result[1] == 12, "Part 2 is wrong"

def test_day_06():
    """Tests that the simple testcase for 2021 day 06 works"""
    from advent_of_code.y2021.day06 import lanternfish
    data = "3,4,3,1,2"
    result = lanternfish(data) 
    assert isinstance(result, tuple)
    assert result[0] == 5934, "Part 1 is wrong"
    assert result[1] == 26984457539, "Part 2 does not work"

def test_day_07():
    """Tests that the simple test case for 2021 day 07 works"""
    from advent_of_code.y2021.day07 import whale_treachery
    data = "16,1,2,0,4,2,7,1,2,14"
    result = whale_treachery(data)
    assert isinstance(result, tuple)
    assert result[0] == 37, "Part 1 is wrong"
    assert result[1] == 168, "Part 2 is wrong"

def test_gaussian_sum():
    """Tests the gaussian sum formula"""
    from advent_of_code.y2021.day07 import gaussian_sum
    for i in range(1, 10001):
        assert gaussian_sum(i) == sum(range(i+1)), "Gaussian sum formula is implemented wrong"


def test_day_08():
    """Tests that the simple test case for 2021 day 8 works"""
    from advent_of_code.y2021.day08 import seven_segment_search

    data = textwrap.dedent("""
        be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
        fdgacbe cefdb cefbgd gcbe
        edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
        fcgedb cgb dgebacf gc
        fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
        cg cg fdcagb cbg
        fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
        efabcd cedba gadfec cb
        aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
        gecf egdcabf bgf bfgea
        fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
        gebdcfa ecba ca fadegcb
        dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
        cefg dcbef fcge gbcadfe
        bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
        ed bcgafe cdgba cbgef
        egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
        gbdfcae bgc cg cgb
        gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
        fgae cfgab fg bagce
    """)
    result = seven_segment_search(data)
    assert isinstance(result, tuple)
    assert result[0] == 26, "Part 1 is wrong"
    assert result[1] != 0, "Part 2 is wrong"
