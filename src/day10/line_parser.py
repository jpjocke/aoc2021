from typing import List

from src.day10.syntax_line import SyntaxLine


def verify_syntax_lines(data: List[str]) -> List[SyntaxLine]:
    syntax_lines = [*map(lambda x: SyntaxLine(x), data)]
    for sl in syntax_lines:
        un_verified = ''
        for c in sl.line:
            if not sl.ok:
                continue
            if __is_open_char(c):
                un_verified += c
            else:
                un_verified = __verify_ending_char(sl, un_verified, c)
        print(sl)
        print(un_verified)
    return syntax_lines


def __verify_ending_char(sl: SyntaxLine, un_verified: str, c: str) -> str:
    open_char_index = __find_open_char(un_verified)
    index = open_char_index[1]
    open_char = open_char_index[0]
    if c == ')':
        if open_char == '(':
            un_verified = un_verified[0:index]
        else:
            sl.ok = False
            sl.errorChar = ')'
    elif c == ']':
        if open_char == '[':
            un_verified = un_verified[0:index]
        else:
            sl.ok = False
            sl.errorChar = ']'
    elif c == '}':
        if open_char == '{':
            un_verified = un_verified[0:index]
        else:
            sl.ok = False
            sl.errorChar = '}'
    elif c == '>':
        if open_char == '<':
            un_verified = un_verified[0:index]
        else:
            sl.ok = False
            sl.errorChar = '>'
    return un_verified


def __find_open_char(parsed: str) -> tuple:
    for i, c in reversed(list(enumerate(parsed))):
        if __is_open_char(c):
            return c, i


def __is_open_char(c: str) -> bool:
    if c == '(' or c == '[' or c == '{' or c == '<':
        return True
    return False
