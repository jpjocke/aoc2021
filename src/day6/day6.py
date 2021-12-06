from file_reader import FileReader
from src.day6.fish_calculator import FishCalculator

fr = FileReader()
data = fr.read_as_str_lines("../../data/day6_in.txt")
d = list(map(int, data[0].split(',')))
fish_calculator = FishCalculator()
one = fish_calculator.calc(d, 80)

print('1: ' + str(one))


fish_calculator = FishCalculator()
two = fish_calculator.calc(d, 256)
print('2: ' + str(two))
# difficulty prob 1 -> 2
# difficulty prob 2 -> 4

