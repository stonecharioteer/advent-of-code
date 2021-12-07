import textwrap


def test_day01():
    """Tests that the simple test case for 2021 day 01 works"""
    from advent_of_code.y2020.day01 import report_repair
    data = textwrap.dedent("""
        1721
        979
        366
        299
        675
        1456
    """)
    data = data.strip().split("\n")
    result = report_repair(data)
    assert isinstance(result, tuple)
    assert result[0] == 514579, "Part 1 is wrong"
    assert result[1] == 241861950, "Part 2 is wrong"

def test_day01_alt():
    """Tests that the simple test case for 2021 day 01 works"""
    from advent_of_code.y2020.day01 import report_repair_itertools
    data = textwrap.dedent("""
        1721
        979
        366
        299
        675
        1456
    """)
    data = data.strip().split("\n")
    result = report_repair_itertools(data)
    assert isinstance(result, tuple)
    assert result[0] == 514579, "Part 1 is wrong"
    assert result[1] == 241861950, "Part 2 is wrong"
