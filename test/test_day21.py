import unittest

from src.day21.board import Board
from src.day21.player import Player


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        p1 = Player(1, 4)
        p2 = Player(2, 8)
        board = Board(10, 1000, [p1, p2])
        score = board.play()
        self.assertEqual(739785, score)

    def test_problem_2(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
