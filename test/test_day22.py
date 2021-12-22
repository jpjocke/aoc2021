import unittest

from src.day22.reactor import calculate_reactor
from src.day22.reactor_parser import parse_reactor
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day22_test_in.txt")
        instructions = parse_reactor(data)
        result = calculate_reactor(instructions, True)
        self.assertEqual(39, result)

    def test_problem_1a(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day22a_test_in.txt")
        instructions = parse_reactor(data)
        result = calculate_reactor(instructions, True)
        self.assertEqual(590784, result)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day22a_test_in.txt")
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
