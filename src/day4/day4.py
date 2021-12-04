from src.day4.controller import Controller
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day4_in.txt")

controller = Controller(data)
controller.run_numbers()
print(str(controller.bingo_board.sum_unmarked()))
print(str(controller.bingo_board.sum_unmarked() * controller.last_number))

# difficulty ?
