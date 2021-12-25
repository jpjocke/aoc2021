import unittest

from binary import Binary
from file_reader import FileReader
from src.day24.alu_parser import parse_alu_data


class TestDay24(unittest.TestCase):
    fr = FileReader()

    def test_problem_eql_1(self):
        alu = parse_alu_data(['inp x', 'eql x 1'])
        alu.add_input(1)
        alu.run()
        self.assertEqual(1, alu.x)

    def test_problem_eql_1(self):
        alu = parse_alu_data(['inp x', 'eql x 1'])
        alu.add_input(2)
        alu.run()
        self.assertEqual(0, alu.x)

    def test_problem_1_binary(self):
        data = self.fr.read_as_str_lines("../data/day24_test_negative.txt")
        alu = parse_alu_data(data)
        alu.add_input(5)
        alu.run()
        self.assertEqual(-5, alu.x)

    def test_problem_1_binary(self):
        data = self.fr.read_as_str_lines("../data/day24_test_binary.txt")
        alu = parse_alu_data(data)
        bin = Binary('1010')
        alu.add_input(bin.as_decimal())
        alu.run()
        self.assertEqual(1, alu.w)
        self.assertEqual(0, alu.x)
        self.assertEqual(1, alu.y)
        self.assertEqual(0, alu.z)

    def test_problem_1(self):
        data = self.fr.read_as_str_lines("../data/day24_in.txt")
        # model_no: 13579246899999
        alu = parse_alu_data(data)
        alu.add_input_list([1, 3, 5, 7, 9, 2, 4, 6, 8, 9, 9, 9, 9, 9])
        alu.run()
        self.assertEqual(0, alu.z)


if __name__ == '__main__':
    unittest.main()
