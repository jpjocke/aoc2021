import unittest

from src.day2.sub_command import SubCommand
from src.day2.submarine import Submarine
from file_reader import FileReader


class TestDayTwo(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day2_test_in.txt")
        commands = [*map(lambda x: SubCommand(x), data)]

        submarine = Submarine()
        for c in commands:
            submarine.run_command(c)
        # code changed for problem 2
        # self.assertEqual(submarine.result(), 150)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day2_test_in.txt")
        commands = [*map(lambda x: SubCommand(x), data)]

        submarine = Submarine()
        for c in commands:
            submarine.run_command(c)
        self.assertEqual(900, submarine.result())


if __name__ == '__main__':
    unittest.main()
