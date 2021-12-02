from enum import Enum


class Command(Enum):
    FORWARD = 1
    DOWN = 2
    UP = 3


class SubCommand:
    direction: Command
    value: int

    def __init__(self, instruction: str):
        split = instruction.split(' ')
        self.value = int(split[1])
        if split[0] == 'forward':
            self.direction = Command.FORWARD
        elif split[0] == 'down':
            self.direction = Command.DOWN
        else:
            self.direction = Command.UP

    def __str__(self) -> str:
        return str(self.direction) + ': ' + str(self.value)
