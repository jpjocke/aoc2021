class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def multiply(self):
        return self.x * self.y

    def __str__(self):
        return 'x: ' + str(self.x) + ', y: ' + str(self.y)
