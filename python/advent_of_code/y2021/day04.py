"""--- Day 4: Giant Squid ---

You're already almost 1.5km (almost a mile) below the surface of the ocean,
already so deep that you can't see any sunlight. What you can see, however, is
a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers.
Numbers are chosen at random, and the chosen number is marked on all boards on
which it appears. (Numbers may not appear on all boards.) If all numbers in any
row or any column of a board are marked, that board wins. (Diagonals don't
count.)

The submarine has a bingo subsystem to help passengers (currently, you and the
giant squid) pass the time. It automatically generates a random order in which
to draw numbers and a random set of boards (your puzzle input). For example:

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

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no
winners, but the boards are marked as follows (shown here adjacent to each
other to save space):

    22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
    8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
    6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
    1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are
still no winners:

    22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
    8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
    6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
    1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

Finally, 24 is drawn:

    22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
    8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
    6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
    1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

At this point, the third board wins because it has at least one complete row or
column of marked numbers (in this case, the entire top row is marked: 14 21 17
24 4).

The score of the winning board can now be calculated. Start by finding the sum
of all unmarked numbers on that board; in this case, the sum is 188. Then,
multiply that sum by the number that was just called when the board won, 24, to
get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win
first. What will your final score be if you choose that board?

--- Part Two ---

On the other hand, it might be wise to try a different strategy: let the giant
squid win.

You aren't sure how many bingo boards a giant squid could play at once, so
rather than waste time counting its arms, the safe thing to do is to figure out
which board will win last and choose that one. That way, no matter which boards
it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after
13 is eventually called and its middle column is completely marked. If you were
to keep playing until this point, the second board would have a sum of unmarked
numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score
be?

"""
from typing import Tuple, Iterable, List


def run(inp: Iterable) -> Tuple[int, int]:
    """Solution for 2021 day 4"""
    data = inp.read().splitlines()
    result = squidgame_bingo_score(data)
    return result

def squidgame_bingo_score(data) -> Tuple[int, int]:
    """Function that solves the squid bingo board problem(s)"""
    random_draw_order = [int(x) for x in data[0].strip().split(",")]
    boards = construct_boards(data[2:])
    part_1 = None
    for draw in random_draw_order:
        for board_index, board in enumerate(boards):
            found_value = board.set_state(draw)
            if found_value:
                if board.has_won:
                    # calculate the score of the board
                    board_unmarked_sum = board.unmarked_sum 
                    part_1 = board_unmarked_sum * draw
            if part_1 is not None:
                break
        if part_1 is not None:
            break
    # solve for part 2
    # note that I can technically do these steps in the first loop itself,
    # but O(N) + O(N) = O(N), since the constant in 2*O(N) doesn't _really_ matter
    part_2 = 0
    # reconstruct the boards for a fresh start
    boards = construct_boards(data[2:])
    # need to lose, so have to find which will win last.
    board_win_order = []
    last_number_call = None
    for draw in random_draw_order:
        for board_index, board in enumerate(boards):
            if board_index not in board_win_order:
                found_value = board.set_state(draw)
                if found_value:
                    if board.has_won:
                        board_win_order.append(board_index)
                        last_number_call = draw
    assert isinstance(last_number_call, int), (
            "There seems to be an error in the loop, it hasn't stored the draw number when the last board won")
    last_board_index = board_win_order[-1]
    last_board_to_win = boards[last_board_index]
    board_unmarked_sum = last_board_to_win.unmarked_sum
    part_2 = board_unmarked_sum * last_number_call

    return (part_1, part_2)


def construct_boards(board_data) -> List:
    """Given a string that contains a collection of bingo boards, this function
    returns a list of boards, which are a multi-dimensional array (5x5)"""
    # boards are split by 2 new lines
    boards_data = "\n".join(board_data).split("\n\n")
    boards = [Board(board) for board in boards_data]
    return boards


class Board:
    """a bingo board object"""

    def __init__(self, board_string):
        self.board_array = self.construct_board(board_string)
        self.marked_array = [[False for _ in range(5)] for _ in range(5)]

    def construct_board(self, board_string):
        """Takes a bingo board string and constructs a 5x5 array"""
        board_array = []
        for line in board_string.split("\n"):
            data = [int(x) for x in line.strip().split()]
            board_array.append(data)
        return board_array
    
    def __repr__(self):
        # reconvert board to string
        board_as_string = "\n\t".join([" ".join([str(x) for x in row]) for row in self.board_array])
        marked_as_string = "\n\t".join([" ".join([str(x) for x in row]) for row in self.marked_array])
        board_string = "Board:\n\t[\n\t{}\n\t]\n\t[\n\t{}\n\t]".format(board_as_string, marked_as_string)
        return board_string

   
    def set_state(self, number) -> bool:
        """checks if a number exists in the board, and if it does, marks it.
        if the number exists, then it returns True, else False"""
        for row, row_values in enumerate(self.board_array):
            for col, value in enumerate(row_values):
                if (value == number) and (self.marked_array[row][col] is False):
                    self.marked_array[row][col] = True
                    return True
        return False

    @property
    def has_won(self) -> bool:
        """Checks if the board is in a 'won' state"""
        for row in range(5):
            row_vals = self.marked_array[row]
            won = all(row_vals)
            if won:
                return True
        for col in range(5):
            col_vals = [self.marked_array[x][col] for x in range(5)]
            won = all(col_vals)
            if won:
                return True
        return False
    
    @property
    def unmarked_sum(self):
        """Calculate the sum of all the unmarked numbers on the board"""
        unmarked_sum = 0
        for row, row_values in enumerate(self.board_array):
            for col, value in enumerate(row_values):
                if self.marked_array[row][col] == False:
                    unmarked_sum += value
        return unmarked_sum
