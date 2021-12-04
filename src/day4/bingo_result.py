from src.day4.bingo_board import BingoBoard


class BingoResult:
    __last_number: int
    __bingo_board: BingoBoard

    def __init__(self, last_number: int, bingo_board: BingoBoard):
        self.__last_number = last_number
        self.__bingo_board = bingo_board

    def get_result(self) -> int:
        return self.__last_number * self.__bingo_board.sum_unmarked()