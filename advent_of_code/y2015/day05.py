"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?
"""

from typing import Iterable, Tuple
import string


def run(inp: Iterable) -> Tuple[int, int]:
    """Returns nice count """
    naughty_words = ["ab", "cd", "pq", "xy"]
    count_nice = 0
    for line in inp:
        line = line.strip()
        if line == "":
            continue

        contains_no_naughty_words = any(word not in line for word in naughty_words)
        contains_3_or_more_vowels = len([vowel for vowel in "aeiou" if vowel in line]) >= 3
        contains_doubles = any(letter*2 in line for letter in string.ascii_lowercase)
        nice = all([contains_no_naughty_words, contains_3_or_more_vowels, contains_doubles])
        if nice:
            count_nice += 1
        print(f"{line=}, {contains_no_naughty_words=}, {contains_3_or_more_vowels=}, {contains_doubles=}")
    return (count_nice, None)
