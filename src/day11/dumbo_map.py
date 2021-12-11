from typing import List

from src.day11.dumbo import Dumbo


class DumboMap:
    __dumbo_map: List[List[Dumbo]]

    def __init__(self, height_map: List[List[Dumbo]]):
        self.__dumbo_map = height_map

    def simulate_one(self) -> bool:
        self.__increase_all()
        run = True
        while run:
            run = self.__increase_all_neighbours()
        return self.__is_synchronized()

    def __is_synchronized(self) -> bool:
        for row in self.__dumbo_map:
            for dumbo in row:
                if dumbo.value <= 9:
                    return False
        return True

    def __increase_all(self):
        for row in self.__dumbo_map:
            for dumbo in row:
                if dumbo.value > 9:
                    dumbo.value = 0
                dumbo.increased_neighbour = False
                dumbo.increase()

    def __increase_all_neighbours(self) -> bool:
        # print(self)
        any_increased = False
        for i, row in enumerate(self.__dumbo_map):
            for j, dumbo in enumerate(row):
                if dumbo.increased_neighbour:
                    continue
                if dumbo.value > 9:
                    any_increased = True
                    self.__increase_neighbours(i, j)
                    dumbo.increased_neighbour = True
        return any_increased

    def __increase_neighbours(self, i: int, j: int):
        # print('im big: ' + str(i) + '-' + str(j) +': ' + self.__dumbo_map[i][j].__str__())
        self.__increase_neighbour(i - 1, j - 1)
        self.__increase_neighbour(i, j - 1)
        self.__increase_neighbour(i + 1, j - 1)
        self.__increase_neighbour(i - 1, j)
        self.__increase_neighbour(i + 1, j)
        self.__increase_neighbour(i - 1, j + 1)
        self.__increase_neighbour(i, j + 1)
        self.__increase_neighbour(i + 1, j + 1)

    def __increase_neighbour(self, i: int, j: int):
        if 0 <= i < len(self.__dumbo_map) and 0 <= j < len(self.__dumbo_map[i]):
            self.__dumbo_map[i][j].increase()
            # print('increase: ' + str(i) + '-' + str(j) + ' -> ' + self.__dumbo_map[i][j].__str__())

    def count_flashes(self) -> int:
        total = 0
        for row in self.__dumbo_map:
            for dumbo in row:
                total += dumbo.flashes
        return total

    def __str__(self):
        sb = ''
        for line in self.__dumbo_map:
            for i in line:
                sb += i.__str__()
            sb += '\n'
        return sb
