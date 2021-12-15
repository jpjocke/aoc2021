from src.day15.path_solver import solve
from src.day15.shortest_path_map_parser import parse_shortest_input
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day15_in.txt")
s_map = parse_shortest_input(data)
s_map = solve(s_map)
for key in s_map:
    print(s_map[key])
print('problem 1: 373 (from print)')
# difficulty ?