from src.day3.gamma_epsilon_calc import GammaEpsilonCalc
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day3_in.txt")

calculator = GammaEpsilonCalc()
calculator.calculate(data)
gamma = calculator.get_gamma()
epsilon = calculator.get_epsilon()

print('problem1: ' + str(gamma.as_decimal() * epsilon.as_decimal()))

# difficulty ?
