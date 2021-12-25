from typing import List, Union

from src.day24.alu import ALU
from src.day24.op import OpMul, OpIn, OpAdd, OpMod, OpDiv, OpEq


def parse_alu_data(data: List[str]) -> ALU:
    alu = ALU()
    for line in data:
        if line.startswith('inp'):
            op = OpIn()
            op.a = line[len(line) - 1]
            alu.add_operator(op)
            continue

        _, a, b = line.split(' ')
        if line.startswith('mul'):
            op = OpMul()
        elif line.startswith('add'):
            op = OpAdd()
        elif line.startswith('mod'):
            op = OpMod()
        elif line.startswith('div'):
            op = OpDiv()
        elif line.startswith('eql'):
            op = OpEq()
        op.a = __convert_number(a)
        op.b = __convert_number(b)
        alu.add_operator(op)

    return alu


def __convert_number(value: str) -> Union[str, int]:
    if value == 'w' or value == 'x' or value == 'y' or value == 'z':
        return value
    return int(value)
