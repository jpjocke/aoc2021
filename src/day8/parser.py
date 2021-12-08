from typing import List

from src.day8.serie import Serie


def remove_empty(series: List[str]) -> List[str]:
    return list(filter(lambda x: len(x) > 0, series))


def parse_line(line: str) -> Serie:
    s1 = line.split('|')
    s2 = s1[0].split(' ')
    series = remove_empty([*map(str, s2)])
    s3 = s1[1].split(' ')
    result = remove_empty([*map(str, s3)])
    return Serie(series, result)
