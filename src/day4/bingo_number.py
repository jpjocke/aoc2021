class BingoNumber:
    number: int
    marked: bool

    def __init__(self, number: int):
        self.number = number
        self.marked = 0

    def mark(self):
        self.marked = 1

    def __str__(self):
        m = '-o-'
        if self.marked == 1:
            m = '-X-'
        return str(self.number) + m
