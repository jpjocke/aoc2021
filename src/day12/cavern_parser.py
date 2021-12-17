from typing import List

from src.day12.cavern import Cavern


def parse_cavern(caverns: List[str]) -> {str, Cavern}:
    key_map = {}
    for cavern in caverns:
        a, b = cavern.split('-')
        if a in key_map:
            c = key_map[a]
        else:
            c = Cavern(a)
            key_map[a] = c
        if b in key_map:
            c1 = key_map[b]
        else:
            c1 = Cavern(b)
            key_map[b] = c1
        c.add_connection(c1)
    return key_map
