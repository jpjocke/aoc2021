import unittest

from day12.cavern_explorer import clean_edges, dfs
from day12.cavern_parser import parse_cavern
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        print('1')
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day12_test_in.txt")
        key_map = parse_cavern(data)
        key_map = clean_edges(key_map)
        length = dfs(key_map, False)
        self.assertEqual(length, 10)

    def test_problem_1b(self):
        print('1a')
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day12b_test_in.txt")
        key_map = parse_cavern(data)
        key_map = clean_edges(key_map)
        length = dfs(key_map, False)
        self.assertEqual(length, 19)

    def test_problem_1c(self):
        print('1c')
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day12c_test_in.txt")
        key_map = parse_cavern(data)
        key_map = clean_edges(key_map)
        length = dfs(key_map, False)
        self.assertEqual(length, 226)

    def test_problem_2(self):
        print('2')
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day12_test_in.txt")
        key_map = parse_cavern(data)
        length = dfs(key_map, True)
        self.assertEqual(length, 36)

    def test_problem_2a(self):
        print('2a')
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day12b_test_in.txt")
        key_map = parse_cavern(data)
        length = dfs(key_map, True)
        self.assertEqual(length, 103)

    def test_problem_2c(self):
        print('2c')
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day12c_test_in.txt")
        key_map = parse_cavern(data)
        length = dfs(key_map, True)
        self.assertEqual(length, 3509)


if __name__ == '__main__':
    unittest.main()
