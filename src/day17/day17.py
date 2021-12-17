from src.day17.area import Area
from point import Point

area = Area(Point(185, -74), Point(221, -122))
y, highest = area.find_highest(100, 500)
amount = area.find_trajectory_count(15, 222, -123, 150)

# too low 4950
print('y:  ' + str(y))
print('problem 1:  ' + str(highest))
# 1036 too low
# 2849 too low
# 2849 too low
# 2925 wrong
print('problem 2:  ' + str(amount))

# difficulty 3
