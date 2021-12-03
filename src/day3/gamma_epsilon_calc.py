from typing import List

from binary import Binary


class GammaEpsilonCalc:
    total: int
    most: List[int]

    def __init__(self):
        self.total = 0
        self.most = []

    def calculate(self, data: List[str]):
        self.total = len(data)
        for i, data_i in enumerate(data):
            for y, char in enumerate(range(len(data_i))):
                print(str(i) + ', ' + data_i + ' - ' + str(y) + ': ' + data_i[y])
                if i == 0:
                    self.most.append(0)
                if data_i[y] == '1':
                    self.most[y] += 1
        print(str(self.total))
        print(*self.most)

    def get_gamma(self) -> Binary:
        value = ''
        for i in range(len(self.most)):
            if self.most[i] > (self.total / 2):
                value += '1'
            else:
                value += '0'
        return Binary(value)

    def get_epsilon(self) -> Binary:
        epsilon = self.get_gamma()
        epsilon.invert()
        return epsilon