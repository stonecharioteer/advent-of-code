from advent_of_code.y2021.day03 import binary_diagonistic


def test_2021_day03():
    """Tests that the simple test case for 2021 day 03 works"""
    import textwrap
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
