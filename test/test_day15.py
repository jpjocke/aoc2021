import unittest

from day15.path_solver import solve_full_djikstra
from day15.shortest_path_map_parser import parse_shortest_input
from file_reader import FileReader
from util import get_key


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day15_test_in.txt")
        s_map = parse_shortest_input(data, 1)
        s_map = solve_full_djikstra(s_map)
        # print_values(s_map, 9, 9)
        # print_path(s_map, 9, 9)
        self.assertEqual(s_map[get_key(9, 9)].path_cost, 40)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day15_test_in.txt")
        s_map = parse_shortest_input(data, 5)
        s_map = solve_full_djikstra(s_map)
        # for key in s_map:
        #    print(s_map[key])
        # print_values(s_map, 49, 49)
        # print_path(s_map, 49, 49)
        self.assertEqual(s_map[get_key(49, 49)].path_cost, 315)

    def test_problem_jos_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day15_jos_in.txt")
        s_map = parse_shortest_input(data, 1)
        s_map = solve_full_djikstra(s_map)
        self.assertEqual(s_map[get_key(99, 99)].path_cost, 811)

    def test_problem_jos_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day15_jos_in.txt")
        s_map = parse_shortest_input(data, 5)
        s_map = solve_full_djikstra(s_map)
        self.assertEqual(s_map[get_key(499, 499)].path_cost, 3012)


if __name__ == '__main__':
    unittest.main()
