from collections import defaultdict

from src.day14.polymer_instruction import PolymerInstruction


class Polymer:
    formula: str
    instructions: dict[str, PolymerInstruction]
    __count_map: dict[str, int]
    __map_of_maps: dict[str, dict[str, int]]

    def __init__(self, formula: str, instructions: dict[str, PolymerInstruction]):
        self.formula = formula
        self.instructions = instructions
        self.__count_map = defaultdict(int)
        self.__map_of_maps = {}

    def calculate(self, iterations: int):
        for i in self.formula:
            self.__count_map[i] += 1
        for i in range(len(self.formula)):
            if i == len(self.formula) - 1:
                break
            self.__calc(self.formula[i] + self.formula[i + 1], iterations)

    def quantity(self) -> int:
        highest = 0
        lowest = 10000000000000
        for key in self.__count_map:
            value = self.__count_map[key]
            if value < lowest:
                lowest = value
            if value > highest:
                highest = value
        return highest - lowest

    def __calc(self, pair: str, iterations: int) -> dict[str, int]:
        if iterations == 0:
            return defaultdict(int)
        iter_key = self.__get_key(pair, iterations)

        # find in cache map
        if iter_key in self.__map_of_maps:
            self.__sum_in_dict(self.__count_map, self.__map_of_maps[iter_key])
            return self.__map_of_maps[iter_key]

        middle = self.instructions[pair].result
        self.__count_map[middle] += 1

        # cache map for this iteration and key pair
        inner_map = defaultdict(int)
        inner_map[middle] += 1

        left = self.__calc(pair[0] + middle, iterations - 1)
        self.__sum_in_dict(inner_map, left)

        right = self.__calc(middle + pair[1], iterations - 1)
        self.__sum_in_dict(inner_map, right)

        # add to cache map
        self.__map_of_maps[iter_key] = inner_map.copy()

        return inner_map

    def __sum_in_dict(self, count_map, left):
        for key in left:
            count_map[key] += left[key]

    def __get_key(self, pair: str, iterations: int) -> str:
        return pair + str(iterations)
