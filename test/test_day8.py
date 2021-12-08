import unittest

from src.day8.parser import parse_line
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day8_test_in.txt")
        series = [*map(parse_line, data)]
        total = 0
        for s in series:
            total += s.count_problem_one()
        self.assertEqual(total, 26)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day8_test_in.txt")
        series = [*map(parse_line, data)]
        total = 0
        for s in series:
            total += s.parse_result()
        self.assertEqual(total, 61229)


if __name__ == '__main__':
    unittest.main()
