from src.day15.path_solver import solve_full_djikstra, print_values
from src.day15.shortest_path_map_parser import parse_shortest_input
from file_reader import FileReader
from util import get_key

fr = FileReader()
data = fr.read_as_str_lines("../../data/day15_in.txt")
s_map = parse_shortest_input(data, 1)
s_map = solve_full_djikstra(s_map)
print('problem 1: 373: ' + s_map[get_key(99, 99)].__str__())

s_map2 = parse_shortest_input(data, 5)
s_map2 = solve_full_djikstra(s_map2)
# 2874 too high
print('problem 2: ' + s_map2[get_key(499, 499)].__str__())
# difficulty 4