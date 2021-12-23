from typing import List

from point import Point


class Amphipod:
    pos: Point
    type: str

    def __init__(self, pos: Point, type: str):
        self.pos = pos
        self.type = type

    def cost_to(self, pos: Point) -> int:
        if self.pos.y == 1 or pos.y == 1:
            return self.pos.distance(pos) * self.move_cost()
        distance = self.pos.distance(Point(self.pos.x, 1))
        distance += Point(self.pos.x, 1).distance(Point(pos.x, 1))
        distance += Point(pos.x, 1).distance(pos)
        return distance * self.move_cost()

    def move_cost(self) -> int:
        if self.type == 'A':
            return 1
        if self.type == 'B':
            return 10
        if self.type == 'C':
            return 100
        return 1000

    def allowed_pos(self) -> List[Point]:
        if self.pos.y != 1:
            allowed = [
                Point(1, 1),
                Point(2, 1),
                Point(4, 1),
                Point(6, 1),
                Point(8, 1),
                Point(10, 1),
                Point(11, 1)
            ]
        else:
            allowed = []
        if self.is_in_end_lane():
            return allowed
        if self.type == 'A':
            allowed.append(Point(3, 2))
            allowed.append(Point(3, 3))
            allowed.append(Point(3, 4))
            allowed.append(Point(3, 5))
        elif self.type == 'B':
            allowed.append(Point(5, 2))
            allowed.append(Point(5, 3))
            allowed.append(Point(5, 4))
            allowed.append(Point(5, 5))
        elif self.type == 'C':
            allowed.append(Point(7, 2))
            allowed.append(Point(7, 3))
            allowed.append(Point(7, 4))
            allowed.append(Point(7, 5))
        elif self.type == 'D':
            allowed.append(Point(9, 2))
            allowed.append(Point(9, 3))
            allowed.append(Point(9, 4))
            allowed.append(Point(9, 5))
        return allowed

    def is_in_end_lane(self) -> bool:
        if self.type == 'A' and self.pos.x == 3:
            return True
        if self.type == 'B' and self.pos.x == 5:
            return True
        if self.type == 'C' and self.pos.x == 7:
            return True
        if self.type == 'D' and self.pos.x == 9:
            return True
        return False

    def __str__(self):
        return self.type + ': ' + self.pos.__str__()