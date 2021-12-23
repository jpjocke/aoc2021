from typing import List

from point import Point
from src.day23.amphipod import Amphipod
from src.day23.hallway import Hallway


def parse_hallway(data: List[str]) -> Hallway:
    hallway = Hallway()
    for y, line in enumerate(data):
        for x, val in enumerate(line):
            if val == 'A' or val == 'B' or val == 'C' or val == 'D':
                pos = Point(x, y)
                amphipod = Amphipod(pos, val)
                hallway.add_amphipod(amphipod)
    return hallway
