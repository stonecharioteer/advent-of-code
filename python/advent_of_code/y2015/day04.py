"""--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
Your puzzle input is ckczppom."""

from typing import Iterable, Tuple
import hashlib

def run(inp: Iterable) -> Tuple[int, int]:
    """Returns number"""
    current = 0
    secret = inp.read()  # TODO: this will fail if it is an iterable. So what is the type really?
    secret = secret.strip()
    answer_5 = None
    answer_6 = None
    while (answer_5 is None) or (answer_6 is None):
        hash_value = hashlib.md5(bytes(f"{secret}{current}", "ascii"))
        hash_value = hash_value.hexdigest()
        if hash_value.startswith("000000") and answer_6 is None:
            answer_6 = current
        elif hash_value.startswith("00000") and answer_5 is None:
            answer_5 = current

        current += 1

    return (answer_5, answer_6)
