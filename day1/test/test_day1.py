import unittest

from depth_measure import DepthMeasure
from util.file_reader import FileReader


class TestDayOne(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_int_lines("../data/day1_test_in.txt")

        dm = DepthMeasure()
        one = dm.count(data)
        self.assertEqual(one, 7)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_int_lines("../data/day1_test_in.txt")

        dm = DepthMeasure()
        spread = dm.spread_list(data, 3)
        two = dm.count(spread)
        self.assertEqual(two, 5)


if __name__ == '__main__':
    unittest.main()
