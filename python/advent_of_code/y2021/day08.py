"""--- Day 8: Seven Segment Search ---
You barely reach the safety of the cave when the whale smashes into the cave
mouth, collapsing it. Sensors indicate another exit to this cave at a much
greater depth, so you have no choice but to press on.

As your submarine slowly makes its way through the cave system, you notice that
the four-digit seven-segment displays in your submarine are malfunctioning;
they must have been damaged during the escape. You'll be in a lot of trouble
without them, so you'd better figure out what's wrong.

Each digit of a seven-segment display is rendered by turning on or off any of
seven segments named a through g:

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

So, to render a 1, only segments c and f would be turned on; the rest would be
off. To render a 7, only segments a, c, and f would be turned on.

The problem is that the signals which control the segments have been mixed up
on each display. The submarine is still trying to display numbers by producing
output on signal wires a through g, but those wires are connected to segments
randomly. Worse, the wire/segment connections are mixed up separately for each
four-digit display! (All of the digits within a display use the same
connections, though.)

So, you might know that only signal wires b and g are turned on, but that
doesn't mean segments b and g are turned on: the only digit that uses two
segments is 1, so it must mean segments c and f are meant to be on. With just
that information, you still can't tell which wire (b/g) goes to which segment
(c/f). For that, you'll need to collect more information.

For each display, you watch the changing signals for a while, make a note of
all ten unique signal patterns you see, and then write down a single four digit
output value (your puzzle input). Using the signal patterns, you should be able
to work out which pattern corresponds to which digit.

For example, here is what you might see in a single entry in your notes:

    acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf

(The entry is wrapped here to two lines so it fits; in your notes, it will all
be on a single line.)

Each entry consists of ten unique signal patterns, a | delimiter, and finally
the four digit output value. Within an entry, the same wire/segment connections
are used (but you don't know what the connections actually are). The unique
signal patterns correspond to the ten different ways the submarine tries to
render a digit using the current wire/segment connections. Because 7 is the
only digit that uses three segments, dab in the above example means that to
render a 7, signal lines d, a, and b are on. Because 4 is the only digit that
uses four segments, eafb means that to render a 4, signal lines e, a, f, and b
are on.

Using this information, you should be able to work out which combination of
signal wires corresponds to each of the ten digits. Then, you can decode the
four digit output value. Unfortunately, in the above example, all of the digits
in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more
difficult to deduce.

For now, focus on the easy digits. Consider this larger example:

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

Because the digits 1, 4, 7, and 8 each use a unique number of segments, you
should be able to tell which combinations of signals correspond to those
digits. Counting only digits in the output values (the part after | on each
line), in the above example, there are 26 instances of digits that use
a unique number of segments (highlighted above).

In the output values, how many times do digits 1, 4, 7, or 8 appear?


{{problem_statement_2 | default("Paste Problem Part 2 here")}}
"""
from typing import Tuple, Iterable


def run(inp: Iterable) -> Tuple[int, int]:
    """Solution for 2021 day 8"""
    data = inp.read().splitlines()
    return seven_segment_search(data)

def seven_segment_search(data):
    """Solves for the seven segment search"""
    part_1 = 0
    part_2 = 0
    # simply count the output values that have a len of 2, 3, 4, or 7
    # since 0, 4, 7, 8 have unique length codes
    for line in data:
        left, right = line.strip().split("|")
        outputs = right.strip().split()
        for output in outputs:
            if len(output) in [2, 3, 4, 7]:
                part_1 += 1
        # need to determine the second part of the solution
    return part_1, part_2


def guess_letter_mapping(inputs):
    """Given an input string for the above problem, this 
    returns a dictionary that maps out the possible values"""
    # first, let's determine what *can* be determined.
    # sort the letters alphabetically. This is not needed,
    # not for this algorithm, but it makes development and
    # debugging easier.
    inputs = ["".join(sorted(x)) for x in inputs]
    # next, sort the array into a list increasing in lengths 
    inputs = sorted(inputs, key=lambda x: len(x))
    # this returns a list that has the following lengths:
    # [2, 3, 4, 5, 5, 5, 6, 6, 6, 7]
    # this corresponds to the following possible values:
    # [1, 7, 4, {2, 3, 5}, {0, 6, 9}, 8]
    # construct a dictionary that holds the values that
    # are possible to guess.
    value_dict = {
            inputs[0]: 1,
            inputs[1]: 7,
            inputs[2]: 4,
            inputs[9]: 8
    }
    # reverse the dict so that we can access the hash with the numbers also.
    rev_dict = dict((value, key) for key, value in value_dict.items())
    # generate a dictionary with keys a-g, with values of None
    cipher = dict((chr(x), None) for x in range(97, 97+7))
    # now try figuring out the key
    # looking at the one letter corresponding to `7` which isn't in `1`:
    # 7 *should* contain acf
    # 1 *should* contain cf
    cipher["a"] = set(rev_dict[7]) - set(rev_dict[1])
    # `a` has been determined, but c and f *can* be one of two values eac
    cipher["c"] = set(rev_dict[7]).intersection(set(rev_dict[1]))
    cipher["f"] = set(rev_dict[7]).intersection(set(rev_dict[1]))
    # now, look at the other possible numbers, 4 and 8
    # 4 *should* contain bcdf
    # 8 *should* contain abcdefg
    # the intersection of 4 with 8 will contain bcdf, and a is known
    intersect_84 = set(rev_dict[8]).intersection(set(rev_dict[4]))
    # remove `a` from this
    intersect_84.discard(list(cipher["a"])[0])
    # this will be either e or f. But we *know* a possible value for f is in
    # cipher_dict["f"]
    # Now, we only loop through the values which are
    # yet undetermined.
    for i_val in inputs:
        print(i_val)
        # Judging by the numbers, you can see which have *common* letters.
        if len(i_val) == 6:
            # if the length is 6, the value could be:
            # 0, 6 or 9
            value = None
            value_dict[i_val] = "none"
            pass
        elif len(i_val) == 5:
            # if the length is 5, the value could be:
            # 2, 3 or 5
            value_dict[i_val] = "none"
            pass
    import ipdb; ipdb.set_trace()
    return cipher
