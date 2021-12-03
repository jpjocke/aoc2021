import unittest

from day3.gamma_epsilon_calc import GammaEpsilonCalc
from day3.oxy_co2_calc import OxyCo2Calc
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day3_test_in.txt")
        calculator = GammaEpsilonCalc(data)
        calculator.calculate_gamma_epsilon()
        gamma = calculator.gamma
        self.assertEqual('10110', gamma.value)
        epsilon = calculator.epsilon
        self.assertEqual('01001', epsilon.value)
        self.assertEqual(gamma.as_decimal() * epsilon.as_decimal(), 198)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day3_test_in.txt")
        oxyCalc = OxyCo2Calc('oxy')
        oxy = oxyCalc.find_binary(data)
        self.assertEqual(23, oxy.as_decimal())
        co2Calc = OxyCo2Calc('co2')
        co2 = co2Calc.find_binary(data)
        self.assertEqual(10, co2.as_decimal())
        self.assertEqual(230, co2.as_decimal() * oxy.as_decimal())


if __name__ == '__main__':
    unittest.main()
