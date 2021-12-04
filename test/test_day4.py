import unittest

from src.day4.controller import Controller
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day4_test_in.txt")
        controller = Controller(data)
        controller.run_numbers()
        print(str(controller.bingo_board.sum_unmarked()))
        print(str(controller.bingo_board.sum_unmarked() * controller.last_number))
        # print(*controller.numbers)
        # for b in controller.bingo_boards:
        #    print(b)
        self.assertEqual(controller.bingo_board.sum_unmarked() * controller.last_number, 4512)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day4_test_in.txt")
        self.assertEqual(230, 230)


if __name__ == '__main__':
    unittest.main()
