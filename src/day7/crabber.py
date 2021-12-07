import math
from functools import reduce
from typing import List


class Crabber:
    # special way of calculating fuel, differ between prob 1 & 2
    power: bool
    crabs: List[int]

    def __init__(self, crabs: List[int], power: bool):
        self.power = power
        self.crabs = crabs
        self.crabs.sort()

    def median(self) -> int:
        middle = math.floor(len(self.crabs) / 2)
        return self.crabs[middle]

    def medium(self) -> int:
        total = reduce(lambda a, b: a + b, self.crabs)
        medium = math.floor(total / len(self.crabs))
        return medium

    def find(self, start: int) -> int:
        smallest_val = self.__find_smallest(start, True)
        down = self.__find_smallest(start - 1, False)
        smallest_val = down if down < smallest_val else smallest_val

        return smallest_val

    def __find_smallest(self, number: int, positive: bool) -> int:
        smallest_val = self.__calc(number)
        while True:
            number = number + 1 if positive else number - 1
            val = self.__calc(number)
            if val > smallest_val:
                break
            else:
                smallest_val = val
        return smallest_val

    def __calc(self, value: int) -> int:
        total = 0
        for crab in self.crabs:
            if self.power:
                val = abs(crab - value)
                for i in range(val):
                    total += i + 1
            else:
                total += abs(crab - value)
        return total
