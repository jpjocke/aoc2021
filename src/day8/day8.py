from src.day8.parser import parse_line
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day8_in.txt")
series = [*map(parse_line, data)]
total_1 = 0
total_2 = 0
for s in series:
    total_1 += s.count_problem_one()
    total_2 += s.parse_result()
print('problem 1: ' + str(total_1))
print('problem 2: ' + str(total_2))
# difficulty 2
