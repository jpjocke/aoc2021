import unittest

from point import Point
from src.day23.hallway_solver import HallwaySolver
from file_reader import FileReader
from src.day23.hallway_parser import parse_hallway


class TestDay23(unittest.TestCase):
    fr = FileReader()

    def test_problem_2(self):
        data = self.fr.read_as_str_lines("../data/day23_test_in.txt")
        hallway = parse_hallway(data)
        solver = HallwaySolver()
        cost = solver.solve(hallway)
        self.assertEqual(44169, cost)

    def test__rule_end_reachable(self):
        data = self.fr.read_as_str_lines("../data/day23/end_reachable.txt")
        hallway = parse_hallway(data)
        moves = hallway.possible_moves()
        self.assertEqual(len(moves), 2)
        self.assertEqual(moves[0][1], Point(3, 5))
        self.assertEqual(moves[0][2], 5)
        self.assertEqual(moves[1][1], Point(5, 5))
        self.assertEqual(moves[1][2], 100)
        solver = HallwaySolver()
        cost = solver.solve(hallway)
        self.assertEqual(105, cost)

    def test__rule_blocked_x4(self):
        data = self.fr.read_as_str_lines("../data/day23/blocked_on_x_4.txt")
        hallway = parse_hallway(data)
        moves = hallway.possible_moves()
        self.assertEqual(len(moves), 1)
        self.assertEqual(moves[0][1], Point(3, 5))
        self.assertEqual(moves[0][2], 5)
        solver = HallwaySolver()
        cost = solver.solve(hallway)
        self.assertEqual(65, cost)

    def test__rule_go_deepest(self):
        data = self.fr.read_as_str_lines("../data/day23/go_deepest.txt")
        hallway = parse_hallway(data)
        moves = hallway.possible_moves()
        self.assertEqual(len(moves), 1)
        self.assertEqual(moves[0][1], Point(5, 4))
        self.assertEqual(moves[0][2], 60)
        solver = HallwaySolver()
        cost = solver.solve(hallway)
        self.assertEqual(1060, cost)

    def test__rule_same_type_in_room(self):
        data = self.fr.read_as_str_lines("../data/day23/same_type_in_room.txt")
        hallway = parse_hallway(data)
        moves = hallway.possible_moves()
        self.assertEqual(len(moves), 1)
        self.assertEqual(moves[0][1], Point(9, 5))
        self.assertEqual(moves[0][2], 10000)
        solver = HallwaySolver()
        cost = solver.solve(hallway)
        self.assertEqual(11860, cost)

if __name__ == '__main__':
    unittest.main()
