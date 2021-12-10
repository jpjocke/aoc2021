import statistics
import unittest

from src.day10.syntax_score import SyntaxScore
from src.day10.line_parser import verify_syntax_lines
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day10_test_in.txt")
        lines = verify_syntax_lines(data)
        score = SyntaxScore(lines)
        self.assertEqual(score.get_error_score(), 26397)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day10_test_in.txt")
        lines = verify_syntax_lines(data)
        score = SyntaxScore(lines)
        self.assertEqual(score.get_valid_score(), 288957)


if __name__ == '__main__':
    unittest.main()
