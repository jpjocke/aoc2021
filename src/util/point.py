from math import floor


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def multiply(self):
        return self.x * self.y

    def __str__(self):
        return 'x: ' + str(self.x) + ', y: ' + str(self.y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __hash__(self):
        x = self.x
        y = self.y
        return floor(((x + y)*(x + y + 1)/2) + y)