from point import Point


class Area:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def find_highest(self, start_y, max_y) -> (int, int):
        largest = 0
        highest = 0
        for y in range(start_y, max_y):
            hit, h = self.__sim_y(y)
            if hit:
                largest = y
                highest = h
        return largest, highest

    def find_x(self):
        for x in range(100):
            if self.__sim_x(x):
                return x

    def __sim_y(self, velocity_y: int) -> (bool, int):
        y = 0
        hit = False
        highest = 0
        while True:
            y += velocity_y
            if y > highest:
                highest = y
            if y < self.end.y:
                break
            if y < self.start.y:
                hit = True
                break
            velocity_y -= 1
        return hit, highest

    def __sim_x(self, velocity_x: int) -> bool:
        x = 0
        hit = False
        while x < self.end.x:
            if x > self.start.x:
                hit = True
                break
            if velocity_x > 0:
                velocity_x -= 1
            if velocity_x < 0:
                velocity_x += 1

            if velocity_x == 0:
                break
            x += velocity_x
        return hit
