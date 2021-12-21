class Player:
    id: int
    pos: int
    score: int

    def __init__(self, id: int, pos: int):
        self.id = id
        self.pos = pos
        self.score = 0

    def __str__(self):
        return str(self.id) + ', pos:' + str(self.pos) + ', score:' + str(self.score)
