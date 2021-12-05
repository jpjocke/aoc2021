from src.day5.line_mapper import LineMapper
from src.day5.line_factory import only_horizontal_or_vertical, to_lines
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day5_in.txt")
lines = only_horizontal_or_vertical(data)
line_mapper = LineMapper()

print('1: ' + str(line_mapper.count_intersections(lines)))

lines = to_lines(data)
print('2: ' + str(line_mapper.count_intersections(lines)))
# difficulty 2
