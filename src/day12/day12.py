from src.day12.cavern_explorer import clean_edges, dfs
from src.day12.cavern_parser import parse_cavern
from file_reader import FileReader

fr = FileReader()
data = fr.read_as_str_lines("../../data/day12_in.txt")
key_map = parse_cavern(data)
key_map = clean_edges(key_map)
length = dfs(key_map, False)
print('problem 1: ' + str(length))
key_map2 = parse_cavern(data)
length2 = dfs(key_map2, True)
print('problem 2: ' + str(length2))

# difficulty 3
