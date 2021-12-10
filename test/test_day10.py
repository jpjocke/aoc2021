import unittest

from src.day10.line_parser import verify_syntax_lines
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day10_test_in.txt")
        lines = verify_syntax_lines(data)
        total = 0
        for l in lines:
            print(l)
            total += l.get_error_point()
        self.assertEqual(total, 26397)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day10_test_in.txt")
        self.assertEqual(1134, 1134)


if __name__ == '__main__':
    unittest.main()
