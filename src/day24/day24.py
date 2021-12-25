from src.day24.threaded_model_no import run_threads
from file_reader import FileReader
from src.day24.alu_parser import parse_alu_data
from src.day24.model_no_tester import test_model_no

fr = FileReader()
data = fr.read_as_str_lines("../../data/day24_in_mod.txt")
alu = parse_alu_data(data)
# TODO threads
#highest = run_threads(alu)
highest = test_model_no(alu, 99999999999999, 30000000000000)
print('problem 1: ' + str(highest))

# difficulty ?
