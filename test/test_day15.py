import unittest

from day15.path_solver import solve
from day15.shortest_path_map_parser import parse_shortest_input
from file_reader import FileReader
from util import get_key


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day15_test_in.txt")
        s_map = parse_shortest_input(data)
        s_map = solve(s_map)
        for key in s_map:
            print(s_map[key])
        self.assertEqual(s_map[get_key(9, 9)].path_cost, 40)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day15_test_in.txt")
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
