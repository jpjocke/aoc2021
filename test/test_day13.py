import unittest

from src.day13.fold_parser import parse_folds
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day13_test_in.txt")
        folder = parse_folds(data)
        folder.fold()
        self.assertEqual(folder.visible(), 16)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day13_test_in.txt")
        self.assertEqual(195, 195)


if __name__ == '__main__':
    unittest.main()
