import unittest

from src.day7.crabber import Crabber
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day7_test_in.txt")
        crabs = list(map(int, data[0].split(',')))
        crabber = Crabber(crabs, False)
        median = crabber.median()
        self.assertEqual(crabber.find(median), 37)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day7_test_in.txt")
        crabs = list(map(int, data[0].split(',')))
        crabber = Crabber(crabs, True)
        medium = crabber.medium()
        self.assertEqual(crabber.find(medium), 168)


if __name__ == '__main__':
    unittest.main()
