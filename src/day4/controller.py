from typing import List

from src.day4.bingo_result import BingoResult
from src.day4.bingo_number import BingoNumber
from src.day4.bingo_board import BingoBoard


class Controller:
    __numbers: List[int]
    __bingo_boards: List[BingoBoard]

    def __init__(self, data: List[str]):
        self.__numbers = []
        self.__bingo_boards = []
        current_board = -1
        for i, row in enumerate(data):
            if i == 0:
                self.__numbers = self.__extract_numbers(row, ',')
            elif row == '':
                current_board += 1
                self.__bingo_boards.append(BingoBoard())
            else:
                numbers = self.__extract_numbers(row, ' ')
                bingo_numbers = [*map(lambda x: BingoNumber(x), numbers)]
                self.__bingo_boards[current_board].add_row(bingo_numbers)

    def run_numbers(self, find_first: bool) -> BingoResult:
        for num in self.__numbers:
            for board in self.__bingo_boards:
                if board.bingo:
                    continue
                board.mark_number(num)
                if board.bingo:
                    if find_first:
                        return BingoResult(num, board)
                    else:
                        if self.__bingo_on_all_boards():
                            return BingoResult(num, board)

    def __bingo_on_all_boards(self) -> bool:
        for inner_board in self.__bingo_boards:
            if not inner_board.bingo:
                return False
        return True

    def __extract_numbers(self, row: str, split: str) -> List[int]:
        numbers = []
        for n in row.split(split):
            # single digits have an extra space in front of them
            if len(n) == 0:
                continue
            numbers.append(int(n))
        return numbers
