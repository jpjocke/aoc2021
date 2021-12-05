import unittest

from src.day5.line_mapper import LineMapper
from src.day5.line_factory import to_lines, only_horizontal_or_vertical
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day5_test_in.txt")
        lines = only_horizontal_or_vertical(data)
        line_mapper = LineMapper()
        self.assertEqual(line_mapper.count_intersections(lines), 5)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day5_test_in.txt")
        lines = to_lines(data)
        line_mapper = LineMapper()
        self.assertEqual(line_mapper.count_intersections(lines), 12)


if __name__ == '__main__':
    unittest.main()
