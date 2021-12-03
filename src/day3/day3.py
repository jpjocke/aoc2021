from src.day3.gamma_epsilon_calc import GammaEpsilonCalc
from src.day3.oxy_co2_calc import OxyCo2Calc
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day3_in.txt")

calculator = GammaEpsilonCalc(data)
calculator.calculate_gamma_epsilon()
gamma = calculator.gamma
epsilon = calculator.epsilon

print('problem1: ' + str(gamma.as_decimal() * epsilon.as_decimal()))


oxyCalc = OxyCo2Calc('oxy')
oxy = oxyCalc.find_binary(data)
co2Calc = OxyCo2Calc('co2')
co2 = co2Calc.find_binary(data)
print('problem2: ' + str(oxy.as_decimal() * co2.as_decimal()))
# difficulty 2
