class Fold:
    value: int
    dir: str

    def __init__(self, dir: str, value: int):
        self.dir = dir
        self.value = value

    def __str__(self):
        return self.dir + ':' + str(self.value)