import unittest

from src.day21.board import Board
from src.day21.part_two import PartTwo
from src.day21.player import Player


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        p1 = Player(1, 4)
        p2 = Player(2, 8)
        board = Board(10, 1000, [p1, p2])
        score = board.play()
        self.assertEqual(739785, score)

    def test_problem_2(self):
        part2 = PartTwo(4, 8, 21)
        self.assertEqual(444356092776315, part2.calculate())


if __name__ == '__main__':
    unittest.main()
