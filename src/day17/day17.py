from src.day17.area import Area
from point import Point

area = Area(Point(185, -74), Point(221, -122))
y, highest = area.find_highest(100, 500)

# too low 4950
print('y:  ' + str(y))
print('problem 1:  ' + str(highest))

# difficulty ?
