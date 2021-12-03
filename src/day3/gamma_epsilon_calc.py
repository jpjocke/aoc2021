from typing import List

from binary import Binary


class GammaEpsilonCalc:
    data: List[str]
    total: int
    most: List[int]
    gamma: Binary
    epsilon: Binary

    def __init__(self, data: List[str]):
        self.total = len(data)
        self.most = []
        self.data = data

    def calculate_gamma_epsilon(self):
        for i, data_i in enumerate(self.data):
            for y, char in enumerate(range(len(data_i))):
                if i == 0:
                    self.most.append(0)
                if data_i[y] == '1':
                    self.most[y] += 1
        self.__set_gamma_epsilon()

    def __set_gamma_epsilon(self):
        self.gamma = self.__calculate_gamma()
        self.epsilon = Binary(self.gamma.value)
        self.epsilon.invert()

    def __calculate_gamma(self) -> Binary:
        value = ''
        for i in range(len(self.most)):
            if self.most[i] >= (self.total / 2):
                value += '1'
            else:
                value += '0'
        return Binary(value)
