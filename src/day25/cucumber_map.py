from typing import List

from point import Point
from src.day25.cucumber import Cucumber


class CucumberMap:
    start: Point
    end: Point
    cucumbers_down: {Point, Cucumber}
    cucumbers_right: {Point, Cucumber}

    def __init__(self, end: Point):
        self.start = Point(0, 0)
        self.end = end
        self.cucumbers_down = {}
        self.cucumbers_right = {}

    def add_cucumber(self, cucumber: Cucumber):
        if cucumber.down:
            self.cucumbers_down[cucumber.pos] = cucumber
        else:
            self.cucumbers_right[cucumber.pos] = cucumber

    def run(self) -> int:
        iterations = 0
        while True:
            print('######################')
            print('######################')
            print(self)
            movers = []
            for key in self.cucumbers_right:
                c = self.cucumbers_right[key]
                next_pos = self.__next_pos(c.pos, c.down)
                if next_pos not in self.cucumbers_right and next_pos not in self.cucumbers_down:
                    movers.append(c)
            moved = True if len(movers) > 0 else False
            self.__move(movers)

            movers = []
            for key in self.cucumbers_down:
                c = self.cucumbers_down[key]
                next_pos = self.__next_pos(c.pos, c.down)
                if next_pos not in self.cucumbers_right and next_pos not in self.cucumbers_down:
                    movers.append(c)
            if not moved:
                moved = True if len(movers) > 0 else False
            self.__move(movers)

            iterations += 1
            if not moved:
                break
            print('------------------------>')
            print(self)

        return iterations

    def __move(self, movers: List[Cucumber]):
        for c in movers:
            next_pos = self.__next_pos(c.pos, c.down)
            if c.down:
                del self.cucumbers_down[c.pos]
                self.cucumbers_down[next_pos] = c
            else:
                del self.cucumbers_right[c.pos]
                self.cucumbers_right[next_pos] = c
            c.pos = next_pos

    def __next_pos(self, pos: Point, down: bool) -> Point:
        if down:
            next_pos = Point(pos.x, pos.y + 1)
            if next_pos.y > self.end.y:
                next_pos.y = 0
            return next_pos
        next_pos = Point(pos.x + 1, pos.y)
        if next_pos.x > self.end.x:
            next_pos.x = 0
        return next_pos

    def __str__(self):
        sb = ''
        for y in range(self.end.y + 1):
            for x in range(self.end.x + 1):
                pos = Point(x, y)
                if pos in self.cucumbers_down:
                    sb += self.cucumbers_down[pos].__str__()
                    continue
                if pos in self.cucumbers_right:
                    sb += self.cucumbers_right[pos].__str__()
                    continue
                sb += '.'
            sb += '\n'
        return sb
