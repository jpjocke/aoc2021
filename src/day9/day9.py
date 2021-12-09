from src.day9.height_map import HeightMap
from src.day9.height_parser import parse_map
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day9_in.txt")
height_map = HeightMap(parse_map(data))
height_map.analyze()
print(height_map)
# 1557 too high
print('problem 1: ' + str(height_map.sum_lows()))

print('problem 2: ' + str(height_map.sum_basins()))

# difficulty 2
