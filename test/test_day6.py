import unittest

from day6.fish_calculator import FishCalculator
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        print('one')
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day6_test_in.txt")
        d = list(map(int, data[0].split(',')))
        fish_calculator = FishCalculator()
        twenty_six = fish_calculator.calc(d, 18)
        self.assertEqual(twenty_six, 26)
        fish_calculator = FishCalculator()
        total = fish_calculator.calc(d, 80)
        self.assertEqual(total, 5934)

    def test_problem_2(self):
        print('two')
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day6_test_in.txt")
        d = list(map(int, data[0].split(',')))
        fish_calculator = FishCalculator()
        total = fish_calculator.calc(d, 256)
        self.assertEqual(total, 26984457539)


if __name__ == '__main__':
    unittest.main()
