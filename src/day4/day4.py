from src.day4.controller import Controller
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day4_in.txt")

controller = Controller(data)
result = controller.run_numbers(1)
print('problem 1: ' + str(result.get_result()))

controller = Controller(data)
result = controller.run_numbers(0)
print('problem 2: ' + str(result.get_result()))
# difficulty 2
