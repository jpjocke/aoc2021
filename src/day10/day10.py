from file_reader import FileReader
from src.day10.line_parser import verify_syntax_lines
from src.day10.syntax_score import SyntaxScore

fr = FileReader()
data = fr.read_as_str_lines("../../data/day10_in.txt")
lines = verify_syntax_lines(data)
score = SyntaxScore(lines)
print('problem 1: ' + str(score.get_error_score()))
print('problem 2: ' + str(score.get_valid_score()))
# difficulty 3
