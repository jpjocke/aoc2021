class Dumbo:
    value: int
    flashes: int
    increased_neighbour: bool

    def __init__(self, value: int):
        self.value = value
        self.flashes = 0
        self.increased_neighbour = False

    def increase(self):
        self.value += 1
        if self.value == 10:
            self.flashes += 1

    def copy(self):
        d = Dumbo(self.value)
        d.flashes = self.flashes
        return d

    def __str__(self):
        sb = ''
        if self.value > 9:
            sb = 'X'
        else:
            sb = str(self.value)
        if self.increased_neighbour:
            sb += '.'
        else:
            sb += ' '
        return sb
