from src.day22.reactor import calculate_reactor
from src.day22.reactor_parser import parse_reactor
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day22_in.txt")
instructions = parse_reactor(data)
result = calculate_reactor(instructions, True)
print('problem 1: ' + str(result))

# difficulty ?
