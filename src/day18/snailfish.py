from typing import Union


class Snailfish:
    left: Union["Snailfish", int]
    right: Union["Snailfish", int]

    def is_left_fish(self) -> bool:
        return not isinstance(self.left, int)

    def is_right_fish(self) -> bool:
        return not isinstance(self.right, int)

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

    def explode(self) -> (int, str):  # returns (rest, > = should go to right | < = should go left)
        if self.__depth_left() >= self.__depth_right():
            # left
            if self.__depth_left() > 1:
                rest, a = self.left.explode()
                if a == '>':
                    print('increase right: ' + str(rest))
                    if not self.is_right_fish():
                        self.right += rest
                    else:
                        self.right.add_left(rest)
                    rest = 0
                return rest, a
            else:
                rest = self.left.left
                self.add_right(self.left.right)
                self.left = 0
                return rest, '<'  # do something
        else:
            # right
            if self.__depth_right() > 1:
                rest, a = self.right.explode()
                if a == '<':
                    print('increase left: ' + str(rest))
                    if not self.is_left_fish():
                        self.left += rest
                    else:
                        self.left.add_right(rest)
                    rest = 0
                return rest, a
            else:
                rest = self.right.right
                self.add_left(self.right.left)
                self.right = 0
                return rest, '>'

    def add_right(self, value: int):
        if self.is_right_fish():
            self.right.add_right(value)
        else:
            self.right += value

    def add_left(self, value: int):
        if self.is_left_fish():
            self.left.add_left(value)
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
