"""--- Day 5: Doesn't He Have Intern-Elves For This? ---
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



--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?


"""

from typing import Counter, TextIO, Tuple
import string


def run(inp: TextIO) -> Tuple[int, int]:
    """Returns nice count """
    naughty_words = ["ab", "cd", "pq", "xy"]
    count_nice_1 = 0
    count_nice_2 = 0
    for line in inp:
        line = line.strip()
        if line == "":
            continue

        contains_no_naughty_words = all(word not in line for word in naughty_words)
        contains_3_or_more_vowels = len([letter for letter in line if letter in "aeiou"]) >= 3
        contains_doubles = any(letter*2 in line for letter in string.ascii_lowercase)
        nice_1 = all([contains_no_naughty_words, contains_3_or_more_vowels, contains_doubles])
        if nice_1:
            count_nice_1 += 1
        twice_pair = False
        for x,y in zip(line[:-1],line[1:]):
            twice_pair = line.count(f"{x}{y}") >= 2
            if twice_pair:
                break
        divided_repeat = False
        for x,y,z in zip(line[:-2], line[1:-1], line[2:]):
            if x == z != y:
                divided_repeat = True
        nice_2 = divided_repeat and twice_pair
        if nice_2:
            count_nice_2 += 1
    return (count_nice_1, count_nice_2)
