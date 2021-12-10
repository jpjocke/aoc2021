from src.day10.line_parser import verify_syntax_lines
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day10_in.txt")
lines = verify_syntax_lines(data)
total = 0
for l in lines:
    total += l.get_error_point()
print('problem 1: ' + str(total))

# difficulty ?
