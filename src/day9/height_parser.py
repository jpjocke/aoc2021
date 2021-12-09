from typing import List

from src.day9.height import Height


def parse_map(raw_map: List[str]) -> List[List[Height]]:
    height_map = []
    for line in raw_map:
        inner_map = []
        for i in line:
            inner_map.append(Height(int(i)))
        height_map.append(inner_map)
    return height_map
