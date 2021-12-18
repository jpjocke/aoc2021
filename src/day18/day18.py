from src.day18.snailfish_math import calculate_snailfish_multiple, calculate_largest_for_two
from src.day18.snailfish_parser import parse_snailfish
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day18_in.txt")
sfs = parse_snailfish(data)
sf = calculate_snailfish_multiple(sfs, False)
print('problem 1:  ' + str(sf.magnitude()))

sfs = parse_snailfish(data)
largest = calculate_largest_for_two(sfs)
# too low: 4380
print('problem 2:  ' + str(largest))
# difficulty 8
