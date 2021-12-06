import unittest

from day6.fish_calculator import calculate_fish
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day6_test_in.txt")
        d = list(map(int, data[0].split(',')))
        twenty_six = calculate_fish(d, 18)
        self.assertEqual(len(twenty_six), 26)
        many = calculate_fish(d, 80)
        self.assertEqual(len(many), 5934)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day6_test_in.txt")
        d = list(map(int, data[0].split(',')))
        # many = calculate_fish(d, 256)
        # self.assertEqual(len(many), 26984457539)


if __name__ == '__main__':
    unittest.main()
