from typing import List


class Cavern:
    identifier: str
    is_small: bool
    is_start: bool = False
    is_end: bool = False
    connections: List["Cavern"]

    def __init__(self, identifier: str):
        self.identifier = identifier
        self.is_small = identifier[0].islower()
        if identifier == 'start':
            self.is_start = True
        if identifier == 'end':
            self.is_end = True
        self.connections = []

    def add_connection(self, cavern: "Cavern"):
        for c in self.connections:
            if c.identifier == cavern.identifier:
                return
        self.connections.append(cavern)
        cavern.add_connection(self)

    def remove_connection(self):
        for c in self.connections:
            c.connections.remove(self)

    def only_small_connections(self) -> bool:
        if len(self.connections) > 1:
            return False
        for c in self.connections:
            if not c.is_small:
                return False
            if c.is_end:
                return False
            if c.is_start:
                return False
        return True

    def __str__(self):
        sb = '['
        for c in self.connections:
            sb += c.identifier + ','
        sb += ']'
        if self.is_small:
            sb += ' -sm'
        else:
            sb += ' -L'
        return self.identifier + ' : ' + sb
