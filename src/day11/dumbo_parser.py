from typing import List

from src.day11.dumbo import Dumbo


def parse_dumbos(raw_map: List[str]) -> List[List[Dumbo]]:
    height_map = []
    for line in raw_map:
        inner_map = []
        for i in line:
            inner_map.append(Dumbo(int(i)))
        height_map.append(inner_map)
    return height_map
