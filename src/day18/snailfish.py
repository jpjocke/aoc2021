from math import floor, ceil
from typing import Union


class Snailfish:
    left: Union["Snailfish", int]
    right: Union["Snailfish", int]

    def is_left_fish(self) -> bool:
        return not isinstance(self.left, int)

    def is_right_fish(self) -> bool:
        return not isinstance(self.right, int)

    def magnitude(self) -> int:
        total = 0
        if self.is_left_fish():
            total += 3 * self.left.magnitude()
        else:
            total += 3 * self.left
        if self.is_right_fish():
            total += 2 * self.right.magnitude()
        else:
            total += 2 * self.right
        return total

    def depth(self) -> int:
        depth_l = 0
        depth_r = 0
        if self.is_left_fish():
            depth_l += self.left.depth() + 1
        if self.is_right_fish():
            depth_r += self.right.depth() + 1
        return depth_l if depth_l > depth_r else depth_r

    def __depth_left(self) -> int:
        depth = 0
        if self.is_left_fish():
            depth += self.left.depth() + 1
        return depth

    def __depth_right(self) -> int:
        depth = 0
        if self.is_right_fish():
            depth += self.right.depth() + 1
        return depth

    def can_explode(self) -> bool:
        if self.depth() > 3:
            return True
        return False

    def can_split(self) -> bool:
        if self.is_left_fish():
            if self.left.can_split():
                return True
        else:
            if self.left >= 10:
                return True
        if self.is_right_fish():
            if self.right.can_split():
                return True
        else:
            if self.right >= 10:
                return True

    def explode(self) -> (int, str):  # returns (rest, > = should go to right | < = should go left)
        if self.__depth_left() >= self.__depth_right():
            # left
            if self.__depth_left() > 1:
                rest, a = self.left.explode()
                if a == '>':
                    if not self.is_right_fish():
                        self.right += rest
                    else:
                        self.right.__add_left(rest)
                    rest = 0
                return rest, a
            else:
                rest = self.left.left
                if not self.is_right_fish():
                    self.right += self.left.right
                else:
                    self.right.__add_left(self.left.right)
                self.left = 0
                return rest, '<'  # do something
        else:
            # right
            if self.__depth_right() > 1:
                rest, a = self.right.explode()
                if a == '<':
                    if not self.is_left_fish():
                        self.left += rest
                    else:
                        self.left.__add_right(rest)
                    rest = 0
                return rest, a
            else:
                rest = self.right.right
                if not self.is_left_fish():
                    self.left += self.right.left
                else:
                    self.left.__add_right()
                self.right = 0
                return rest, '>'

    def split(self):
        if self.is_left_fish():
            if self.left.can_split():
                self.left.split()
                return
        else:
            if self.left >= 10:
                l = floor(self.left / 2)
                r = ceil(self.left / 2)
                self.left = Snailfish()
                self.left.left = l
                self.left.right = r
                return
        if self.is_right_fish():
            if self.right.can_split():
                self.right.split()
                return
        else:
            if self.right >= 10:
                l = floor(self.right / 2)
                r = ceil(self.right / 2)
                self.right = Snailfish()
                self.right.left = l
                self.right.right = r
                return

    def __add_right(self, value: int):
        if self.is_right_fish():
            self.right.__add_right(value)
        else:
            self.right += value

    def __add_left(self, value: int):
        if self.is_left_fish():
            self.left.__add_left(value)
        else:
            self.left += value

    def __str__(self):
        sb = '['
        if isinstance(self.left, int):
            sb += str(self.left)
        else:
            sb += self.left.__str__()
        sb += ','
        if isinstance(self.right, int):
            sb += str(self.right)
        else:
            sb += self.right.__str__()
        return sb + ']'
