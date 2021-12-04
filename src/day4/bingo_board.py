from typing import List

from src.day4.bingo_number import BingoNumber


class BingoBoard:
    rows: List[List[BingoNumber]]
    bingo: bool

    def __init__(self):
        self.rows = []
        self.bingo = 0

    def add_row(self, row: List[BingoNumber]):
        self.rows.append(row)

    def mark_number(self, number: int):
        marked = 0
        for row in self.rows:
            for num in row:
                if num.number == number:
                    num.mark()
                    marked = 1
                    break
            if marked == 1:
                break
        self.__check_bingo()

    def sum_unmarked(self) -> int:
        total = 0
        for row in self.rows:
            for num in row:
                if num.marked == 0:
                    total += num.number
        return total

    def __check_bingo(self):
        for i in range(len(self.rows)):
            if self.__check_row_bingo(i):
                self.bingo = 1
                break

        for i in range(len(self.rows[0])):
            if self.__check_column_bingo(i):
                self.bingo = 1
                break

    def __check_row_bingo(self, index: int) -> bool:
        for num in self.rows[index]:
            if num.marked == 0:
                return 0
        return 1

    def __check_column_bingo(self, index: int) -> bool:
        for row in self.rows:
            if row[index].marked == 0:
                return 0
        return 1

    def __str__(self):
        ret = ''
        for row in self.rows:
            for num in row:
                ret += num.__str__() + ' '
            ret += '\n'
        return ret
