from src.day7.crabber import Crabber
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day7_in.txt")
crabs = list(map(int, data[0].split(',')))
crabber = Crabber(crabs, False)
median = crabber.median()
print('median: ' + str(median))
smallest = crabber.find(median)
print('problem 1: ' + str(smallest))

crabber = Crabber(crabs, True)
medium = crabber.medium()
print('medium: ' + str(medium))
smallest = crabber.find(medium)
print('problem 2: ' + str(smallest))
# difficulty 1
