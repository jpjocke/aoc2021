from typing import List

from line import Line
from point import Point


def __to_point(p: str) -> Point:
    xy = p.split(',')
    return Point(int(xy[0]), int(xy[1]))


def to_lines(data: List[str]) -> List[Line]:
    lines = []
    for data in data:
        raw_split = data.split(' ')
        point1 = __to_point(raw_split[0])
        point2 = __to_point(raw_split[2])
        lines.append(Line(point1, point2))

    return lines


def only_horizontal_or_vertical(data: List[str]) -> List[Line]:
    lines = to_lines(data)
    return list(filter(lambda x: x.is_horizontal() or x.is_vertical(), lines))
