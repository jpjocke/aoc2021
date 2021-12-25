from point import Point


class Cucumber:
    pos: Point
    down: bool

    def __init__(self, pos: Point, down: bool):
        self.pos = pos
        self.down = down

    def __str__(self):
        if self.down:
            return 'v'
        else:
            return '>'
