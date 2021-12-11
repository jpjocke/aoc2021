from src.day11.dumbo_map import DumboMap
from src.day11.dumbo_parser import parse_dumbos
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day11_in.txt")
dumbos = parse_dumbos(data)
dumbo_map = DumboMap(dumbos)
for i in range(100):
    dumbo_map.simulate_one()
print(dumbo_map)
flashes = dumbo_map.count_flashes()
print('problem 1: ' + str(flashes))

dumbos2 = parse_dumbos(data)
dumbo_map2 = DumboMap(dumbos2)
sims = 0
synced = False
while not synced:
    sims += 1
    synced = dumbo_map2.simulate_one()
    print(dumbo_map2)
# 132 too low
# 133 too low
print('problem 2: ' + str(sims))
# difficulty ?
