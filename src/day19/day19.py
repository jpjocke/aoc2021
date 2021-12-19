from file_reader import FileReader
from src.day19.beacon_map import BeaconMap
from src.day19.scanner_parser import parse_scanners

fr = FileReader()
data = fr.read_as_str_lines("../../data/day19_in.txt")
scanners = parse_scanners(data)
beacon_map = BeaconMap(scanners)
count = beacon_map.calculate_map()

# too high: 419
print('problem 1:  ' + str(count))
print('problem 2: ' + str(beacon_map.longest_manhattan()))
# difficulty 6
