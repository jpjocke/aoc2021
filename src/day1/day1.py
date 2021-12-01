from src.day1.depth_measure import DepthMeasure
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_int_lines("../../data/day1_in.txt")

dm = DepthMeasure()
one = dm.count(data)
print("problem 1: " + str(one))

spread = dm.spread_list(data, 3)
two = dm.count(spread)
print("problem 2: " + str(two))

# difficulty: easy
