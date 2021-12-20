from typing import List

from point import Point
from src.day20.image import Image
from util import get_key


def parse_image(data: List[str]) -> Image:
    first = True
    algo = ''
    y = 0
    image = Image()
    image.min = Point(0, 0)
    for line in data:
        if len(line) == 0:
            first = False
            continue
        if first:
            algo += line
        else:
            for x, val in enumerate(line):
                image.image[get_key(x, y)] = 1 if val == '#' else 0
            y += 1
    image.algo = algo
    image.max = Point(len(data[len(data) - 1]), y)
    return image
