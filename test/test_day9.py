import unittest

from src.day9.height_map import HeightMap
from src.day9.height_parser import parse_map
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day9_test_in.txt")
        height_map = HeightMap(parse_map(data))
        print(height_map)
        height_map.analyze()
        print('--')
        print(height_map)
        self.assertEqual(height_map.sum_lows(), 15)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day9_test_in.txt")
        height_map = HeightMap(parse_map(data))
        self.assertEqual(1134, 1134)


if __name__ == '__main__':
    unittest.main()
