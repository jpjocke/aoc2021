from typing import List

from line import Line
from point import Point


class LineMapper:

    def count_intersections(self, lines: List[Line]) -> int:
        intersection_map = dict({})
        intersections = 0
        for line in lines:
            for pos in line.get_line():
                key = pos.__str__()
                if key in intersection_map:
                    intersection_map[key] += intersection_map[key]
                    if intersection_map[key] == 2:
                        intersections += 1
                else:
                    intersection_map[key] = 1

        return intersections

    def __get_key(self, p: Point) -> str:
        return str(p.x) + '-' + str(p)
