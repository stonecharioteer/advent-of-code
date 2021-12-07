"""--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport; the easiest way
down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
"Something's wrong with our computers; we can't log in!" You ask if you can
take a look.

Their password database seems to be a little corrupted: some of the passwords
wouldn't have been allowed by the Official Toboggan Corporate Policy that was
in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of
passwords (according to the corrupted database) and the corporate policy when
that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy
indicates the lowest and highest number of times a given letter must appear for
the password to be valid. For example, 1-3 a means that the password must
contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is
not; it contains no instances of b, but needs at least 1. The first and third
passwords are valid: they contain one a or nine c, both within the limits of
their respective policies.

How many passwords are valid according to their policies?


{{problem_statement_2 | default("Paste Problem Part 2 here")}}
"""
from typing import Tuple, Iterable


def run(inp: Iterable) -> Tuple[int, int]:
    """Solution for 2020 day 2"""
    data = inp.read().splitlines()
    result = password_philosophy(data)
    return result


def password_philosophy(password_record):
    """Validates passwords according to the rules"""
    from collections import Counter
    valid = 0
    for line in password_record:
        prefix, suffix = line.split("-")
        min_count = int(prefix)
        max_count = int(suffix[:suffix.find(" ")])
        letter = suffix[suffix.find(" ")+1:suffix.find(":")]
        input_password = suffix.split(":")[1].strip()
        letter_count = Counter(input_password)
        if min_count <= letter_count[letter] <= max_count:
            valid += 1
    return valid, None
