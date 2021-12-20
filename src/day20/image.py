from collections import defaultdict

from binary import Binary
from point import Point
from util import get_key


class Image:
    algo: str
    image: {str, int}
    min: Point
    max: Point

    def __init__(self):
        self.image = defaultdict(int)

    def enhance(self):
        next_min = Point(self.min.x - 1, self.min.y - 1)
        next_max = Point(self.max.x + 1, self.max.y + 1)
        next_image = defaultdict(int)
        for y in range(next_min.y, next_max.y):
            for x in range(next_min.x, next_max.x):
                next_image[get_key(x, y)] = self.__get_bit(x, y)
        self.min = next_min
        self.max = next_max
        self.image = next_image

    def __get_bit(self, x: int, y: int) -> int:
        sb = ''
        sb += str(self.image[get_key(x - 1, y - 1)])
        sb += str(self.image[get_key(x, y - 1)])
        sb += str(self.image[get_key(x + 1, y - 1)])
        sb += str(self.image[get_key(x - 1, y)])
        sb += str(self.image[get_key(x, y)])
        sb += str(self.image[get_key(x + 1, y)])
        sb += str(self.image[get_key(x - 1, y + 1)])
        sb += str(self.image[get_key(x, y + 1)])
        sb += str(self.image[get_key(x + 1, y + 1)])
        b = Binary(sb)
        val = 1 if self.algo[b.as_decimal()] == '#' else 0
        # print(get_key(x, y) + ': ' + b.value + ' = ' + str(b.as_decimal()) + ' = ' + str(val))
        return val

    def count(self) -> int:
        total = 0
        for key in self.image:
            total += self.image[key]
        return total

    def __str__(self):
        sb = ''
        for y in range(self.min.y, self.max.y):
            for x in range(self.min.x, self.max.x):
                sb += '#' if self.image[get_key(x, y)] == 1 else '.'
            sb += '\n'
        return sb
