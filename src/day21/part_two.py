from typing import List


class PartTwo:
    a_start: int
    b_start: int
    max_score: int
    result_map = {str, List[int]}

    def __init__(self, a: int, b: int, max_score: int):
        self.a_start = a
        self.b_start = b
        self.max_score = max_score
        self.result_map = {}

    def calculate(self) -> int:
        a, b = self.__calc(self.a_start, self.b_start, 0, 0, True)
        return a if a > b else b

    def __calc(self, a_pos: int, b_pos: int, a_score: int, b_score: int, a_turn: bool) -> [int, int]:
        key = self.__key(a_pos, b_pos, a_score, b_score, a_turn)
        if key in self.result_map:
            return self.result_map[key]

        result = [0, 0]
        for roll1 in range(1, 4):
            for roll2 in range(1, 4):
                for roll3 in range(1, 4):
                    roll = roll1 + roll2 + roll3
                    wins = self.__calc2(a_pos, b_pos, a_score, b_score, a_turn, roll)
                    result[0] += wins[0]
                    result[1] += wins[1]
        self.result_map[key] = result
        return result

    def __calc2(self, a_pos: int, b_pos: int, a_score: int, b_score: int, a_turn: bool, roll: int) -> [int, int]:
        if a_turn:
            a_pos = self.__adjust_pos(a_pos, roll)
            a_score += a_pos
            if a_score >= self.max_score:
                return [1, 0]
            else:
                return self.__calc(a_pos, b_pos, a_score, b_score, False)
        else:
            b_pos = self.__adjust_pos(b_pos, roll)
            b_score += b_pos
            if b_score >= self.max_score:
                return [0, 1]
            else:
                return self.__calc(a_pos, b_pos, a_score, b_score, True)

    def __key(self, a_pos: int, b_pos: int, a_score: int, b_score: int, a_turn: bool) -> str:
        return '(' + str(a_pos) + ':' + str(a_score) + ')(' + str(b_pos) + ':' + str(b_score) + ')-' + (
            'A' if a_turn else 'B')

    def __adjust_pos(self, pos: int, roll: int) -> int:
        pos += roll
        if pos > 10:
            pos -= 10
        return pos
