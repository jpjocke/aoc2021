import unittest

from point import Point
from src.day17.area import Area


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        area = Area(Point(20, -5), Point(30, -10))
        y, highest = area.find_highest(0, 10)
        self.assertEqual(y, 9)
        self.assertEqual(highest, 45)
        self.assertEqual(area.find_x(), 7)

    def test_problem_2(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
