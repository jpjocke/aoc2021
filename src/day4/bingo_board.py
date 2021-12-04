from typing import List

from src.day4.bingo_number import BingoNumber


class BingoBoard:
    __rows: List[List[BingoNumber]]
    bingo: bool

    def __init__(self):
        self.__rows = []
        self.bingo = False

    def add_row(self, row: List[BingoNumber]):
        self.__rows.append(row)

    def mark_number(self, number: int):
        found = False
        for row in self.__rows:
            for num in row:
                if num.number == number:
                    num.mark()
                    found = True
                    break
            if found:
                break
        self.__check_bingo()

    def sum_unmarked(self) -> int:
        total = 0
        for row in self.__rows:
            for num in row:
                if not num.marked:
                    total += num.number
        return total

    def __check_bingo(self):
        for i in range(len(self.__rows)):
            if self.__check_row_bingo(i):
                self.bingo = True
                break

        for i in range(len(self.__rows[0])):
            if self.__check_column_bingo(i):
                self.bingo = True
                break

    def __check_row_bingo(self, index: int) -> bool:
        for num in self.__rows[index]:
            if not num.marked:
                return False
        return True

    def __check_column_bingo(self, index: int) -> bool:
        for row in self.__rows:
            if not row[index].marked:
                return False
        return True

    def __str__(self):
        string_builder = ''
        for row in self.__rows:
            for num in row:
                string_builder += num.__str__() + ' '
            string_builder += '\n'
        return string_builder
