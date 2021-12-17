from src.day16.parse_hex_package import parse_hex_package
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day16_in.txt")
packages = parse_hex_package(data[0])
p = packages[0]

print('problem 1:  ' + str(p.version_value()))
print('problem 2:  ' + str(p.calculate()))

# difficulty 3
