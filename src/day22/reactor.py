from typing import List, Set

from point3D import Point3D
from src.day22.reactor_instruction import ReactorInstruction


def calculate_reactor(instructions: List[ReactorInstruction], ignore_large: bool) -> int:
    on_set = set([])
    for instruction in instructions:
        if ignore_large:
            if __is_large(instruction):
                continue
        __run_instruction(on_set, instruction.start, instruction.end, instruction.on)
    return len(on_set)


def __run_instruction(on_set: Set, start: Point3D, end: Point3D, add: bool):
    for x in range(start.x, end.x + 1):
        for y in range(start.y, end.y + 1):
            for z in range(start.z, end.z + 1):
                p = Point3D(x, y, z)
                if add:
                    on_set.add(p)
                else:
                    if p in on_set:
                        on_set.remove(p)


def __is_large(instruction: ReactorInstruction) -> bool:
    if __pos_is_large(instruction.start):
        return True
    return __pos_is_large(instruction.end)


def __pos_is_large(pos: Point3D) -> bool:
    if pos.x < -50 or pos.x > 50:
        return True
    if pos.y < -50 or pos.y > 50:
        return True
    if pos.z < -50 or pos.z > 50:
        return True
