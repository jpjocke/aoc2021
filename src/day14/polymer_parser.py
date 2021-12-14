from typing import List

from src.day14.polymer_instruction import PolymerInstruction
from src.day14.polymer import Polymer


def parse_polymer(data: List[str]) -> Polymer:
    formula = ''
    instructions = {}
    for i, row in enumerate(data):
        if i == 0:
            formula = row
        if i > 1:
            a, b = row.split(' -> ')
            pi = PolymerInstruction(a, b)
            instructions[pi.formula] = pi
    return Polymer(formula, instructions)