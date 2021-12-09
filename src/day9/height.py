class Height:
    value: int
    low: bool

    def __init__(self, value: int):
        self.value = value
        self.low = False

    def __str__(self):
        low = 'o' if self.low else '.'
        return str(self.value) + low
