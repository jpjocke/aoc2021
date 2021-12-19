from src.day19.beacon_map import BeaconMap
from src.day19.scanner_parser import parse_scanners
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day19_in.txt")
scanners = parse_scanners(data)
beacon_map = BeaconMap(scanners)
count = beacon_map.calculate_map()

# too high: 419
print('problem 1:  ' + str(count))

# difficulty ?
