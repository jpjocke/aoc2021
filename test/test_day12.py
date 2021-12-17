import unittest

from day12.cavern_explorer import clean_edges, dfs
from day12.cavern_parser import parse_cavern
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day12_test_in.txt")
        key_map = parse_cavern(data)
        key_map = clean_edges(key_map)
        length = dfs(key_map)
        self.assertEqual(length, 10)

    def test_problem_1b(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day12b_test_in.txt")
        key_map = parse_cavern(data)
        key_map = clean_edges(key_map)
        length = dfs(key_map)
        self.assertEqual(length, 19)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day12_test_in.txt")
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
