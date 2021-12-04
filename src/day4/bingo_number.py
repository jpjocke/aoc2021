class BingoNumber:
    number: int
    marked: bool

    def __init__(self, number: int):
        self.number = number
        self.marked = False

    def mark(self):
        self.marked = True

    def __str__(self):
        m = '-o-'
        if self.marked:
            m = '-X-'
        return str(self.number) + m
