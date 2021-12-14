import unittest

from src.day14.polymer_parser import parse_polymer
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day14_test_in.txt")
        polymer = parse_polymer(data)
        polymer.calculate(10)
        self.assertEqual(polymer.quantity(), 1588)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day14_test_in.txt")
        #polymer = parse_polymer(data)
        #polymer.calculate(40)
        self.assertEqual(polymer.quantity(), 2188189693529)


if __name__ == '__main__':
    unittest.main()
