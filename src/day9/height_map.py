from typing import List

from src.day9.height import Height


class HeightMap:
    __height_map: List[List[Height]]

    def __init__(self, height_map: List[List[Height]]):
        self.__height_map = height_map

    def analyze(self):
        for i, row in enumerate(self.__height_map):
            for j, val in enumerate(row):
                val.low = self.__is_low(i, j, val.value)

    def sum_lows(self) -> int:
        total = 0
        for row in self.__height_map:
            for val in row:
                total += val.value + 1 if val.low else 0
        return total

    def __is_low(self, i: int, j: int, val: int) -> bool:
        # up
        if i > 0:
            if self.__height_map[i - 1][j].value <= val:
                return False
        # down
        if i < len(self.__height_map) - 1:
            if self.__height_map[i + 1][j].value <= val:
                return False
        # left
        if j > 0:
            if self.__height_map[i][j - 1].value <= val:
                return False
        # right
        if j < len(self.__height_map[i]) - 1:
            if self.__height_map[i][j + 1].value <= val:
                return False
        return True

    def __str__(self):
        sb = ''
        for line in self.__height_map:
            for i in line:
                sb += i.__str__() + ' '
            sb += '\n'
        return sb
