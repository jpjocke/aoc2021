from typing import List


class Node:
    identifier: str
    cost: int
    path_cost: int
    checked: bool
    from_path: object
    paths: List[object]

    def __init__(self, identifier: str, cost: int):
        self.identifier = identifier
        self.cost = cost
        self.path_cost = 999999999999999
        self.checked = False
        self.paths = []
        self.from_path = None

    def __str__(self):
        sb = self.identifier + ', ' + str(self.cost) + ' ['
        for key in self.paths:
            sb += key.identifier + ', '
        sb += '] = ' + str(self.path_cost)
        if self.from_path is not None:
            sb += ' from: ' + self.from_path.identifier
        return sb
