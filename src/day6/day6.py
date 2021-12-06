from src.day6.fish_calculator import calculate_fish
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day6_in.txt")
d = list(map(int, data[0].split(',')))
eighty = calculate_fish(d, 80)

print('1: ' + str(len(eighty)))
# difficulty ?
