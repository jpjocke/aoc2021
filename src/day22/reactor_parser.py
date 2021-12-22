from typing import List

from point3D import Point3D
from src.day22.reactor_instruction import ReactorInstruction


def parse_reactor(data: List[str]) -> List[ReactorInstruction]:
    instructions = []
    for line in data:
        instruction = ReactorInstruction()
        # on x=-20..33,y=-21..23,z=-26..28
        on, ins = line.split(' ')
        instruction.on = True if on == 'on' else False
        # x=-20..33,y=-21..23,z=-26..28
        x, y, z = ins.split(',')
        xs, xe = __parse_start_end(x)
        ys, ye = __parse_start_end(y)
        zs, ze = __parse_start_end(z)
        start = Point3D(xs, ys, zs)
        end = Point3D(xe, ye, ze)
        instruction.start = start
        instruction.end = end
        instructions.append(instruction)
    return instructions


def __parse_start_end(line: str) -> (int, int):
    # x=-20..33
    _, v = line.split('=')
    s, e = v.split('..')
    return int(s), int(e)
