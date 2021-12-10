import statistics
from typing import List

from src.day10.syntax_line import SyntaxLine


class SyntaxScore:
    syntax_lines: List[SyntaxLine]

    def __init__(self, syntax_lines: List[SyntaxLine]):
        self.syntax_lines = syntax_lines

    def get_error_score(self) -> int:
        total = 0
        for l in self.syntax_lines:
            if not l.ok:
                total += l.get_error_point()
        return total

    def get_valid_score(self) -> int:
        score_list = []
        for l in self.syntax_lines:
            if l.ok:
                score_list.append(l.get_complete_point())
        return statistics.median(score_list)
