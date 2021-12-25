import math
from typing import Union, List


class Operator:
    a: Union[str, int]
    b: Union[str, int]

    def run(self, a: int, b: int) -> int:
        return a

    def __type(self) -> str:
        return 'no type'

    def __str__(self):
        return self.__type() + ' ' + str(self.a) + ' ' + str(self.b)


class OpIn(Operator):
    def input(self, inputs: List[int], input_order: int) -> int:
        return inputs[input_order]

    def __type(self) -> str:
        return 'inp'

    def __str__(self):
        return self.__type() + ' ' + str(self.a)


class OpAdd(Operator):
    def run(self, a: int, b: int) -> int:
        return a + b

    def __type(self) -> str:
        return 'add'

    def __str__(self):
        return self.__type() + ' ' + str(self.a) + ' ' + str(self.b)


class OpMul(Operator):
    def run(self, a: int, b: int) -> int:
        return a * b

    def __type(self) -> str:
        return 'mul'

    def __str__(self):
        return self.__type() + ' ' + str(self.a) + ' ' + str(self.b)


class OpDiv(Operator):
    def run(self, a: int, b: int) -> int:
        if b == 0:
            raise Exception('divide by 0')
        return math.floor(a / b)

    def __type(self) -> str:
        return 'div'

    def __str__(self):
        return self.__type() + ' ' + str(self.a) + ' ' + str(self.b)


class OpMod(Operator):
    def run(self, a: int, b: int) -> int:
        if a < 0:
            raise Exception('mod a less than 0')
        if b < 0:
            raise Exception('mod b less than 0')
        return a % b

    def __type(self) -> str:
        return 'mod'

    def __str__(self):
        return self.__type() + ' ' + str(self.a) + ' ' + str(self.b)


class OpEq(Operator):
    def run(self, a: int, b: int) -> int:
        return 1 if a == b else 0

    def __type(self) -> str:
        return 'eql'

    def __str__(self):
        return self.__type() + ' ' + str(self.a) + ' ' + str(self.b)
