import unittest

from day3.gamma_epsilon_calc import GammaEpsilonCalc
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day3_test_in.txt")
        calculator = GammaEpsilonCalc()
        calculator.calculate(data)
        gamma = calculator.get_gamma()
        self.assertEqual(gamma.value, '10110')
        epsilon = calculator.get_epsilon()
        self.assertEqual(epsilon.value, '01001')
        self.assertEqual(gamma.as_decimal() * epsilon.as_decimal(), 198)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day3_test_in.txt")
        self.assertEqual(900, 900)


if __name__ == '__main__':
    unittest.main()
