from typing import List

from src.day4.bingo_number import BingoNumber
from src.day4.bingo_board import BingoBoard


class Controller:
    numbers: List[int]
    bingo_boards: List[BingoBoard]
    last_number: int
    bingo_board: BingoBoard

    def __init__(self, data: List[str]):
        self.numbers = []
        self.bingo_boards = []
        current_board = -1
        for i, row in enumerate(data):
            if i == 0:
                self.numbers = self.__extract_numbers(row, ',')
            elif row == '':
                current_board += 1
                self.bingo_boards.append(BingoBoard())
            else:
                numbers = self.__extract_numbers(row, ' ')
                bingo_numbers = []
                for y in numbers:
                    bingo_numbers.append(BingoNumber(y))
                self.bingo_boards[current_board].add_row(bingo_numbers)

    def run_numbers(self):
        for num in self.numbers:
            self.last_number = num
            for board in self.bingo_boards:
                board.mark_number(num)
                if board.bingo == 1:
                    print('BINGO')
                    print('number: ' + str(self.last_number))
                    print(board)
                    self.bingo_board = board
                    return

    def __extract_numbers(self, row: str, split: str) -> List[int]:
        numbers = []
        for n in row.split(split):
            if len(n) == 0:
                continue
            numbers.append(int(n))
        return numbers
