from src.day20.image_parser import parse_image
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day20_in.txt")
image = parse_image(data)
p1 = 0
for i in range(50):
    image.enhance()
    if i == 1:
        p1 = image.count()
p2 = image.count()
# too high: 5464
print('problem 1: ' + str(p1))
print('problem 2: ' + str(p2))
# difficulty 3
