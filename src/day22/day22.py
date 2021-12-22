from file_reader import FileReader
from src.day22.reactor_naive import calculate_reactor_naive
from src.day22.reactor_parser import parse_reactor

fr = FileReader()
data = fr.read_as_str_lines("../../data/day22_in.txt")
instructions = parse_reactor(data)
result = calculate_reactor_naive(instructions, True)
print('problem 1: ' + str(result))

# difficulty ?
