from src.day21.board import Board
from src.day21.part_two import PartTwo
from src.day21.player import Player

p1 = Player(1, 6)
p2 = Player(2, 8)
board = Board(10, 1000, [p1, p2])
score = board.play()
print('problem 1: ' + str(score))

part2 = PartTwo(6, 8, 21)
score2 = part2.calculate()
# too low: 444356092776315
print('problem 2: ' + str(score2))
# difficulty 4
