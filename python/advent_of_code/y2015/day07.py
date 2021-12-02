"""
--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?


--- Part Two ---
Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?


"""

from typing import TextIO, Tuple


def evaluate(a, b, operator):
    if operator == "AND":
        return a & b
    elif operator == "OR":
        return a | b
    elif operator == "LSHIFT":
        return a << b
    elif operator == "RSHIFT":
        return a >> b


def run(inp: TextIO) -> Tuple[int, int]:
    """Day 7 solution"""
    import copy
    data_dict_1 = {}
    for line in inp:
        line = line.strip()
        if line == "":
            continue
        lhs, rhs = line.split("->")
        lhs = lhs.strip()
        rhs = rhs.strip()
        data_dict_1[rhs] = {
            "expression": lhs,
            "value": None if not lhs.isnumeric() else int(lhs)
        }
    data_dict_2 = copy.deepcopy(data_dict_1)

    def compute(data_dict):
        unsolved = True
        i = 0
        while unsolved:
            for key in data_dict:
                if data_dict[key]["value"] is not None:
                    continue
                expression = data_dict[key]["expression"]
                if expression.isnumeric():
                    print(expression)
                    data_dict[key]["value"] = int(expression)
                elif expression.startswith("NOT"):
                    player = expression.replace("NOT", "").strip()
                    val = data_dict[player]["value"]
                    if val is not None:
                        data_dict[key]["value"] = ~ val
                else:
                    if "AND" in expression:
                        operator = "AND"
                    elif "OR" in expression:
                        operator = "OR"
                    elif "LSHIFT" in expression:
                        operator = "LSHIFT"
                    elif "RSHIFT" in expression:
                        operator = "RSHIFT"
                    else:
                        val = data_dict[expression]["value"]
                        if val is not None:
                            data_dict[key]["value"] = val
                        continue

                    player_a, player_b = expression.split(operator)
                    player_a = player_a.strip()
                    player_b = player_b.strip()

                    if player_a.isnumeric():
                        val_a = int(player_a)
                    else:
                        val_a = data_dict[player_a]["value"]

                    if player_b.isnumeric():
                        val_b = int(player_b)
                    else:
                        val_b = data_dict[player_b]["value"]
                    if val_a is not None and val_b is not None:
                        data_dict[key]["value"] = evaluate(val_a, val_b, operator)
            unsolved = len([key for key in data_dict if data_dict[key]["value"] is None]) > 0
            i += 1
        return data_dict
    data_dict_1 = compute(data_dict_1)
    part_1 = data_dict_1["a"]["value"]
    data_dict_2["b"]["value"] = part_1
    data_dict_2 = compute(data_dict_2)
    part_2 = data_dict_2["a"]["value"]

    return (part_1, part_2)
