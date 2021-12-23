from file_reader import FileReader
from src.day23.hallway_parser import parse_hallway
from src.day23.hallway_solver import HallwaySolver

fr = FileReader()
data = fr.read_as_str_lines("../../data/day23_in.txt")
print('problem 1: 10321 (solved by hand)')
hallway = parse_hallway(data)
solver = HallwaySolver()
cost = solver.solve(hallway)
print('problem 2: ' + str(cost))

# difficulty 6
