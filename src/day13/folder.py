from typing import List

from src.day13.fold import Fold
from point import Point


class Folder:
    positions: List[Point]
    folds: List[Fold]

    def __init__(self):
        self.positions = []
        self.folds = []

    def add_pos(self, point: Point):
        self.positions.append(point)

    def add_fold(self, fold: Fold):
        self.folds.append(fold)

    def fold(self):
        for fold in self.folds:
            print(fold)
            # print(len(self.positions))
            for pos in self.positions:
                # print(pos)
                if fold.dir == 'y':
                    if pos.y < fold.value:
                        # print('skip y')
                        continue
                    pos.y = fold.value - (pos.y - fold.value)
                else:
                    if pos.x < fold.value:
                        # print('skip x')
                        continue
                    pos.x = fold.value - (pos.x - fold.value)
                # print(pos)
            self.positions = list(set(self.positions))
            # print(len(self.positions))
            print(self)

    def visible(self) -> int:
        return len(self.positions)

    def __str__(self):
        max_x = 0
        max_y = 0
        for pos in self.positions:
            if pos.x > max_x:
                max_x = pos.x
            if pos.y > max_y:
                max_y = pos.y
        if max_x > 40 or max_y > 40:
            return 'too big'
        sb = ''
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                found = False
                for pos in self.positions:
                    if x == pos.x and y == pos.y:
                        found = True
                        break
                if found:
                    sb += '#'
                else:
                    sb += '.'
            sb += '\n'
        return sb
