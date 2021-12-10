from typing import List

from src.day10.syntax_line import SyntaxLine


def verify_syntax_lines(data: List[str]) -> List[SyntaxLine]:
    syntax_lines = [*map(lambda x: SyntaxLine(x), data)]
    for sl in syntax_lines:
        un_verified = []
        for c in sl.line:
            if not sl.ok:
                continue
            if __is_open_char(c):
                un_verified.append(c)
            else:
                un_verified = __verify_ending_char(sl, un_verified, c)
        if sl.ok:
            __complete_line(sl, un_verified)
    return syntax_lines


def __complete_line(sl: SyntaxLine, un_verified: List[str]):
    for c in reversed(un_verified):
        if c == '(':
            sl.completed += ')'
        elif c == '[':
            sl.completed += ']'
        elif c == '{':
            sl.completed += '}'
        elif c == '<':
            sl.completed += '>'


def __verify_ending_char(sl: SyntaxLine, un_verified: List[str], c: str) -> List[str]:
    last_char = un_verified[len(un_verified) - 1]
    error = True
    if c == ')':
        if last_char == '(':
            error = False
    elif c == ']':
        if last_char == '[':
            error = False
    elif c == '}':
        if last_char == '{':
            error = False
    elif c == '>':
        if last_char == '<':
            error = False
    if error:
        sl.ok = False
        sl.errorChar = c
    else:
        un_verified.pop()

    return un_verified


def __is_open_char(c: str) -> bool:
    if c == '(' or c == '[' or c == '{' or c == '<':
        return True
    return False
