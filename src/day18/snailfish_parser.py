from typing import List

from src.day18.snailfish import Snailfish

__START = '['
__END = ']'


def parse_snailfish(data: List[str]) -> List[Snailfish]:
    snailfishes = []
    for line in data:
        sf = __parse_one(line)
        snailfishes.append(sf)
    return snailfishes


def __parse_one(data: str) -> Snailfish:
    pair_raw = data[1:len(data) - 1]
    start = pair_raw[0]
    end = pair_raw[len(pair_raw) - 1]
    sf = Snailfish()
    if start == __START:  # left is pair
        end_left = 0
        count = 0
        for i, x in enumerate(pair_raw):
            if x == __START:
                count += 1
            if x == __END:
                count -= 1
            if count == 0:
                end_left = i + 1
                break
        sf.left = __parse_one(pair_raw[0:end_left])
    else:
        # support 2 digits only
        if pair_raw[1] != ',':
            start += pair_raw[1]
        sf.left = int(start)

    if end == __END:  # right is pair
        start_right = 0
        count = 0
        for i, x in reversed(list(enumerate(pair_raw))):
            if x == __END:
                count += 1
            if x == __START:
                count -= 1
            if count == 0:
                start_right = i
                break
        sf.right = __parse_one(pair_raw[start_right::])
    else:
        if pair_raw[len(pair_raw) - 2] != ',':
            end = pair_raw[len(pair_raw) - 2] + end
        sf.right = int(end)
    return sf
