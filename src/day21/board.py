from typing import List

from src.day21.deterministic_die import DeterministicDie
from src.day21.player import Player


class Board:
    __size: int
    __max_score: int
    __players: List[Player]
    __current_player: int
    __die: DeterministicDie

    def __init__(self, size: int, max_score: int, players: List[Player]):
        self.__size = size
        self.__max_score = max_score
        self.__players = players
        self.__current_player = 0
        self.__die = DeterministicDie()

    def play(self) -> int:
        while True:
            rolls = [self.__die.next(), self.__die.next(), self.__die.next()]
            die_roll = sum(rolls)
            # print('rolled: ' + str(rolls[0]) + '+' + str(rolls[1]) + '+' + str(rolls[2]) + '=' + str(die_roll) + ', %10 =' + str(die_roll % 10))
            p = self.__players[self.__current_player]
            p.pos += (die_roll % self.__size)
            if p.pos > self.__size:
                p.pos -= self.__size
            p.score += p.pos
            # print(p.__str__() + ' rolled: ' + str(die_roll))

            if p.score >= self.__max_score:
                print(p.__str__() + ' wins')
                other_player = 0 if self.__current_player == 1 else 1
                return self.__players[other_player].score * self.__die.rolls
            self.__current_player = 0 if self.__current_player == 1 else 1
