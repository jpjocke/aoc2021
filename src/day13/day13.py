from src.day13.fold_parser import parse_folds
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day13_in.txt")
folder = parse_folds(data)
folder.fold()
# first fold = 653
# wrong: 102 (all folds)
print('problem 1: ' + str(folder.visible()))
print('problem 2: ' + 'LKREBPRK')
# difficulty 3
