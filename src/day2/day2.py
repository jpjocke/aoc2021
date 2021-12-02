from src.day2.submarine import Submarine
from src.day2.sub_command import SubCommand
from file_reader import FileReader

fr = FileReader()
data2 = fr.read_as_str_lines("../../data/day2_in.txt")
commands = [*map(lambda x: SubCommand(x), data2)]

submarine = Submarine()
for c in commands:
    submarine.run_command(c)

# problem 2 changed functionality, cant do problem 1
print('problem 2: ' + str(submarine.result()))

# difficulty easy
