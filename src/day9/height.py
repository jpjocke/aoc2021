class Height:
    value: int
    low: bool
    basin: bool

    def __init__(self, value: int):
        self.value = value
        self.low = False
        self.basin = False

    def __str__(self):
        if not self.low and not self.basin:
            return str(self.value)
        if self.low:
            return 'x'
        return '.'
