from src.day20.image_parser import parse_image
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day20_in.txt")
image = parse_image(data)
print(image)
image.enhance()
print('---')
print(image)
image.enhance()
print('---')
print(image)

# too high: 5464
print('problem 1: ' + str(image.count()))
# difficulty ?
