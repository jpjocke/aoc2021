from src.day14.polymer_parser import parse_polymer
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day14_in.txt")
polymer = parse_polymer(data)
polymer.calculate(10)
print('problem 1: ' + str(polymer.quantity()))
polymer2 = parse_polymer(data)
polymer2.calculate(40)
print('problem 2: ' + str(polymer2.quantity()))
