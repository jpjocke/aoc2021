from collections import defaultdict

from src.day14.polymer_instruction import PolymerInstruction


class Polymer:
    formula: str
    instructions: dict[str, PolymerInstruction]
    count_map: dict[str, int]
    map_of_maps: dict[str, dict[str, int]]

    def __init__(self, formula: str, instructions: dict[str, PolymerInstruction]):
        self.formula = formula
        self.instructions = instructions
        self.count_map = defaultdict(int)

    def calculate(self, iterations: int):
        for i in self.formula:
            self.count_map[i] += 1
        for i in range(len(self.formula)):
            if i == len(self.formula) - 1:
                break
            self.__calc(self.formula[i] + self.formula[i + 1], iterations)

    def quantity(self) -> int:
        highest = 0
        lowest = 10000000000000
        for key in self.count_map:
            value = self.count_map[key]
            if value < lowest:
                lowest = value
            if value > highest:
                highest = value
        return highest - lowest

    def __calc(self, pair: str, iterations: int):
        # print(pair + ' - ' + str(iterations))
        if iterations == 0:
            return
        middle = self.instructions[pair].result
        print(pair + ' -> ' + pair[0] + middle + pair[1])
        self.count_map[middle] += 1
        self.__calc(pair[0] + middle, iterations - 1)
        self.__calc(middle + pair[1], iterations - 1)
