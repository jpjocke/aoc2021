from typing import List

from binary import Binary
from src.day3.gamma_epsilon_calc import GammaEpsilonCalc


class OxyCo2Calc:
    mode: str

    def __init__(self, mode: str):
        # todo
        # if mode != 'co2' && mode != 'oxy':
        #     raise
        self.mode = mode

    def find_binary(self, data: List[str]) -> Binary:
        bit = 0
        while len(data) > 1:
            binary = self.__get_binary_for_data(data)
            data = list(filter(lambda x: x[bit] == binary.value[bit], data))
            bit += 1
        return Binary(data[0])

    def __get_binary_for_data(self, data: List[str]) -> Binary:
        calculator = GammaEpsilonCalc(data)
        calculator.calculate_gamma_epsilon()
        # oxygen -> gamma
        if self.mode == 'oxy':
            return calculator.gamma
        # co2 scrubber -> epsilon
        return calculator.epsilon
