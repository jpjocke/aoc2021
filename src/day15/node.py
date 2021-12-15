from math import floor
from typing import Set

from util import unwind_key


class Node:
    identifier: str
    cost: int
    path_cost: int
    checked: bool
    from_path: "Node"
    paths: Set["Node"]

    def __init__(self, identifier: str, cost: int):
        self.identifier = identifier
        self.cost = cost
        self.path_cost = 999999999999999
        self.checked = False
        self.paths = set([])
        self.from_path = None

    def add_path(self, node: object):
        self.paths.add(node)

    def show_path(self) -> str:
        if self.from_path is None:
            return '.'
        x, y = unwind_key(self.identifier)
        x1, y1 = unwind_key(self.from_path.identifier)
        # weird coordinates
        if x == x1:
            if y1 < y:
                return '←'  # '↑'
            else:
                return '→'  # '↓'
        if x1 < x:
            return '↑'  # '←'
        return '↓'  # '→'

    def __str__(self):
        sb = self.identifier + ', ' + str(self.cost) + ' ['
        for key in self.paths:
            sb += key.identifier + ', '
        sb += '] = ' + str(self.path_cost)
        if self.from_path is not None:
            sb += ' from: ' + self.from_path.identifier
        return sb

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented

        return self.identifier == other.identifier

    def __hash__(self):
        x, y = unwind_key(self.identifier)
        return floor(((x + y) * (x + y + 1) / 2) + y)
