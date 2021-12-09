from functools import reduce
from typing import List

from src.day9.height import Height


class HeightMap:
    __height_map: List[List[Height]]
    __basin_map: {}

    def __init__(self, height_map: List[List[Height]]):
        self.__height_map = height_map
        self.__basin_map = {}

    def analyze(self):
        for i, row in enumerate(self.__height_map):
            for j, val in enumerate(row):
                val.low = self.__is_low(i, j, val.value)
                if not val.basin and val.value != 9:
                    key = str(i) + '-' + str(j)
                    size = self.__explore_basin(i, j)
                    self.__basin_map[key] = size

    def sum_lows(self) -> int:
        total = 0
        for row in self.__height_map:
            for val in row:
                total += val.value + 1 if val.low else 0
        return total

    def sum_basins(self) -> int:
        largest = [0, 0, 0]
        for key in self.__basin_map:
            val = self.__basin_map[key]
            if val > largest[0]:
                largest[2] = largest[1]
                largest[1] = largest[0]
                largest[0] = val
            elif val > largest[1]:
                largest[2] = largest[1]
                largest[1] = val
            elif val > largest[2]:
                largest[2] = val
        return reduce(lambda a, b: a * b, largest)

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

    # recursive exploration
    def __explore_basin(self, i: int, j: int) -> int:
        if self.__height_map[i][j].value == 9:
            return 0
        if self.__height_map[i][j].basin:
            return 0
        total = 1
        self.__height_map[i][j].basin = True
        # up
        if i > 0:
            total += self.__explore_basin(i - 1, j)
        # down
        if i < len(self.__height_map) - 1:
            total += self.__explore_basin(i + 1, j)
        # left
        if j > 0:
            total += self.__explore_basin(i, j - 1)
        # right
        if j < len(self.__height_map[i]) - 1:
            total += self.__explore_basin(i, j + 1)
        return total

    def __str__(self):
        sb = ''
        for line in self.__height_map:
            for i in line:
                sb += i.__str__()
            sb += '\n'
        return sb
