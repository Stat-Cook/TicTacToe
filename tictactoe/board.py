import numpy as np
from typing import List

class Board:

    def __init__(self, blank=" "):
        self.blank = blank
        self.moves = None
        self.reset_moves()

    def reset_moves(self):
        """ Remove all moves from game state """
        self.moves = [[self.blank for _ in range(3)] for _ in range(3)]

    def draw_board(self):
        """ Display current game state """
        is_first = True
        for row in self.moves:
            if is_first:
                is_first = False
            else:
                print("-"*5)

            print("|".join(row))

    def add_move(self, symbol, index):
        """ Insert a symbol into the game board """
        corrected_index = index - 1
        row = corrected_index // 3
        column = corrected_index % 3

        if self.moves[row][column] == self.blank:
            self.moves[row][column] = symbol
            return True

        raise(AttributeError("Already taken"))

    def check_for_victory(self):
        moves = np.array(self.moves)

        row_checks = self.check_by_row(moves)
        if row_checks:
            return row_checks

        column_checks = self.check_by_row(moves.T)
        if column_checks:
            return column_checks

        diag_1 = self.check_diagonal(moves)
        if diag_1:
            return diag_1

        diag_2 = self.check_diagonal(moves.T)
        if diag_2:
            return diag_2

        return ""

    def check_by_row(self, matrix):
        """ Check every row of a matrix for win condition"""
        victory = [i for i, row in enumerate(matrix) if self.victory_rule(row)]

        if len(victory) == 0:
            return ""

        return matrix[victory[0]][0]

    def check_diagonal(self, matrix):
        """ Check the diagonal a matrix for win condition"""

        if not isinstance(matrix, np.ndarray):
            matrix = np.array(matrix)

        vec = matrix.reshape(9)

        if self.victory_rule(vec[[0, 4, 8]]):
            return vec[0]

        if self.victory_rule(vec[[2, 4, 6]]):
            return vec[2]

        return ""

    def victory_rule(self, vec: List):
        """ Check a list of 3 values for win condition """
        if vec[0] == self.blank:
            return False

        if (vec[0] == vec[1]) & (vec[0] == vec[2]):
            return True

        return False


if __name__ == '__main__':
    b1 = Board()
    b1.draw_board()

    [b1.add_move("X", i) for i in [3, 5, 7]]
    b1.draw_board()
    print(b1.check_for_victory())

