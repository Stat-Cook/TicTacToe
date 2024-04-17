import unittest
from tictactoe.board import Board
import numpy as np

class TestBoard(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board()
        self.fail_examples = [
            [" ", " ", " "],
            ["X", "X", " "],
            ["X", "O", " "],
            ["O", "X", " "],
            ["O", "X", "O"]
        ]
        self.victory_examples = [
            ["X", "X", "X"],
            ["O", "O", "O"]
        ]

        self.victory_move_indices = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7]
        ]

    def test_add_move(self):
        self.board.add_move("X", 1)
        self.assertEqual(["X", " ", " "], self.board.moves[0])
        self.assertEqual([" ", " ", " "], self.board.moves[1])

        self.board.add_move("X", 2)
        self.assertEqual(["X", "X", " "], self.board.moves[0])
        self.assertEqual([" ", " ", " "], self.board.moves[1])

        self.board.add_move("X", 5)
        self.assertEqual([" ", "X", " "], self.board.moves[1])

        self.board.add_move("X", 9)
        self.assertEqual([" ", " ", "X"], self.board.moves[2])

        with self.assertRaises(AttributeError):
            self.board.add_move("X", 9)

        self.assertEqual([" ", " ", "X"], self.board.moves[2])

    def test_reset_moves(self):
        self.board.add_move("X", 1)
        self.assertEqual(["X", " ", " "], self.board.moves[0])

        self.board.reset_moves()
        self.assertEqual([" ", " ", " "], self.board.moves[0])

    def test_victory_rule(self):
        self.assertTrue(self.board.victory_rule(["X", "X", "X"]))
        self.assertTrue(self.board.victory_rule(["O", "O", "O"]))

        self.assertFalse(self.board.victory_rule([" ", " ", " "]))
        self.assertFalse(self.board.victory_rule(["X", "X", " "]))
        self.assertFalse(self.board.victory_rule(["X", "O", " "]))
        self.assertFalse(self.board.victory_rule(["O", "X", " "]))
        self.assertFalse(self.board.victory_rule(["O", "X", "O"]))

    def test_check_by_row(self):
        self.assertEqual("", self.board.check_by_row(self.fail_examples))

        self.fail_examples.insert(2, ["X", "X", "X"])
        self.assertEqual(
            "X",
            self.board.check_by_row(self.fail_examples)
        )

        self.fail_examples[2] = ["O", "O", "O"]
        self.assertEqual(
            "O",
            self.board.check_by_row(self.fail_examples)
        )

    def test_check_diagonal(self):
        self.assertEqual(
            "",
            self.board.check_diagonal(self.board.moves)
        )

        self.board.moves[0][0] = "X"
        self.board.moves[1][1] = "X"
        self.board.moves[2][2] = "X"

        self.assertEqual(
            "X",
            self.board.check_diagonal(self.board.moves)
        )

        self.board.reset_moves()
        self.board.moves[0][0] = "X"
        self.board.moves[1][1] = "X"
        self.board.moves[2][2] = "X"

        board_array = np.array(self.board.moves)
        self.assertEqual(
            "X",
            self.board.check_diagonal(board_array)
        )

    def test_check_for_victory(self):
        self.assertEqual(
            "",
            self.board.check_for_victory()
        )

        for indices in self.victory_move_indices:
            self.board.reset_moves()
            for i in indices:
                self.board.add_move("X", i)

            self.assertEqual(
                "X",
                self.board.check_for_victory()
            )

