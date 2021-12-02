from src.day2.sub_command import SubCommand, Command
from point import Point


class Submarine:
    position: Point
    aim: int

    def __init__(self):
        self.position = Point(0, 0)
        self.aim = 0

    def run_command(self, command: SubCommand):
        if command.direction == Command.FORWARD:
            self.position.x += command.value
            self.position.y += command.value * self.aim
        elif command.direction == Command.DOWN:
            self.aim += command.value
        else:
            self.aim -= command.value

    def result(self):
        return self.position.multiply()

    def __str__(self):
        return 'Position: ' + self.position.__str__() + ', aiming at: ' + str(self.aim)
