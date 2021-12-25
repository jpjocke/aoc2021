from typing import List

from point import Point
from src.day25.cucumber import Cucumber
from src.day25.cucumber_map import CucumberMap


def parse_cucumbers(data: List[str]) -> CucumberMap:
    c_map = CucumberMap(Point(len(data[0]) - 1, len(data) - 1))
    for y, line in enumerate(data):
        for x, val in enumerate(line):
            if val == '>':
                c_map.add_cucumber(Cucumber(Point(x, y), False))
            elif val == 'v':
                c_map.add_cucumber(Cucumber(Point(x, y), True))
    return c_map
