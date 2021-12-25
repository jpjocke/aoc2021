from src.day25.cucumber_parser import parse_cucumbers
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day25_in.txt")
c_map = parse_cucumbers(data)
moves = c_map.run()
print('problem 1: ' + str(moves))

# difficulty 3
