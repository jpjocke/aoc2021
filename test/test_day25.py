import unittest

from src.day25.cucumber_parser import parse_cucumbers
from file_reader import FileReader


class TestDay25(unittest.TestCase):
    fr = FileReader()

    def test_problem_1_binary(self):
        data = self.fr.read_as_str_lines("../data/day25_test_in.txt")
        c_map = parse_cucumbers(data)
        moves = c_map.run()
        self.assertEqual(58, moves)


if __name__ == '__main__':
    unittest.main()
