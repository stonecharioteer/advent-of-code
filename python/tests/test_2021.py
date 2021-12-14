# vim: set foldmethod=indent:
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
        be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
        edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
        fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
        fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
        aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
        fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
        dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
        bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
        egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
        gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
    """)
    data = data.strip().split("\n")
    result = seven_segment_search(data)
    assert isinstance(result, tuple)
    assert result[0] == 26, "Part 1 is wrong"
    assert result[1] == 61229, "Part 2 is wrong"


def test_day_09():
    """Tests that the simple test case for 2021 09 works"""
    from advent_of_code.y2021.day09 import smoke_basin
    data = textwrap.dedent("""
        2199943210
        3987894921
        9856789892
        8767896789
        9899965678
    """)
    data = data.strip().split()
    result = smoke_basin(data)
    assert isinstance(result, tuple)
    part_1, part_2 = result
    assert part_1 == 15, "Part 1 is wrong"
    assert part_2 == 1134, "Part 2 is wrong"


def test_get_neighbors():
    """Tests the neighbors calculation algorithm for day 9 (BFS)"""
    from advent_of_code.y2021.day09 import get_neighbors
    matrix = [[0 for _ in range(10)] for _ in range(5)]
    # left corner 
    assert get_neighbors(matrix, (0,0)) == set([(0,1), (1,0)])
    # some point in the middle
    assert get_neighbors(matrix, (1,1)) == set([(1,2), (0,1), (1,0), (2,1)])
    # point just before the right
    assert get_neighbors(matrix, (1,8)) == set([(0,8), (2,8), (1,9), (1, 7)])
    # point just before the right
    assert get_neighbors(matrix, (3,1)) == set([(3,0), (2,1), (3,2), (4,1)])
    # right corner
    assert get_neighbors(matrix, (0,9)) == set([(0,8), (1,9)])


def test_day_10():
    """Tests that the simple test case for 2021 10 works"""
    from advent_of_code.y2021.day10 import syntax_scoring
    data = textwrap.dedent("""
        [({(<(())[]>[[{[]{<()<>>
        [(()[<>])]({[<{<<[]>>(
        {([(<{}[<>[]}>{[]{[(<()>
        (((({<>}<{<{<>}{[]{[]{}
        [[<[([]))<([[{}[[()]]]
        [{[{({}]{}}([{[{{{}}([]
        {<[[]]>}<{[{[{[]{()[[[]
        [<(<(<(<{}))><([]([]()
        <{([([[(<>()){}]>(<<{{
        <{([{{}}[<[[[<>{}]]]>[]]
    """)
    data = data.strip().split("\n") 
    result = syntax_scoring(data)
    assert isinstance(result, tuple)
    part_1, part_2 = result
    assert part_1 == 26397, "Part 1 is wrong"
    assert part_2 == 288957, "Part 2 is wrong"


def test_day_11_simple():
    """Tests that the simple test case for 2021 11 works"""
    from advent_of_code.y2021.day11 import Point, Grid
    data = textwrap.dedent("""
        11111
        19991
        19191
        19991
        11111
    """)
    data = data.strip().split("\n")
    matrix = [[int(x) for x in line] for line in data]
    points = [[Point(y, x, val) for y, val in enumerate(row) ] for x, row  in enumerate(matrix)]
    grid = Grid(points, max_level=9)
    flashed = grid.advance(1)
    assert flashed == 9, "the flashed check algorithm is wrong for a simple case for a simple case for a simple case for a simple case"

def test_day_11():
    """Tests that the simple test case for 2021 11 works"""
    from advent_of_code.y2021.day11 import dumb_octopus
    data = textwrap.dedent("""
        5483143223
        2745854711
        5264556173
        6141336146
        6357385478
        4167524645
        2176841721
        6882881134
        4846848554
        5283751526
    """)
    data = data.strip().split("\n")
    result = dumb_octopus(data)
    assert isinstance(result, tuple), "Result should have been a tuple"
    part_1, part_2 = result
    assert part_1 == 1656, "Part 1 is wrong"
    assert part_2 == 195, "Part 2 is wrong"

def test_day_12():
    """Tests that the simple test case for 2021 12 works"""
    from advent_of_code.y2021.day12 import solution
    data = textwrap.dedent("""
        dc-end
        HN-start
        start-kj
        dc-start
        dc-HN
        LN-dc
        HN-end
        kj-sa
        kj-HN
        kj-dc
    """)
    data = data.split("\n")
    result = solution(data)
    assert isinstance(result, tuple), "Result should have been a tuple"
    part_1, part_2 = result
    assert part_1 == 226, "Part 1 is wrong"
    assert part_2 == 0, "Part 2 is wrong"


def test_template():
    """Tests that the simple test case for 2021 {} works"""
    from advent_of_code.y2021.day import solution
    data = textwrap.dedent("""
    """)
    data = data.split("\n")
    result = solution(data)
    assert isinstance(result, tuple), "Result should have been a tuple"
    part_1, part_2 = result
    raise NotImplementedError("Part 1 is not implemented!")
    assert part_1 == 0, "Part 1 is wrong"
    assert part_2 == 0, "Part 2 is wrong"
