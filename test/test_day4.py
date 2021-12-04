import unittest

from src.day4.controller import Controller
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day4_test_in.txt")
        controller = Controller(data)
        result = controller.run_numbers(1)
        self.assertEqual(result.get_result(), 4512)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day4_test_in.txt")
        controller = Controller(data)
        result = controller.run_numbers(0)
        self.assertEqual(result.get_result(), 1924)


if __name__ == '__main__':
    unittest.main()
