from src.day21.board import Board
from src.day21.player import Player

p1 = Player(1, 6)
p2 = Player(2, 8)
board = Board(10, 1000, [p1, p2])
score = board.play()
print('problem 1: ' + str(score))
# difficulty ?
