from typing import List

from src.day18.snailfish import Snailfish


# TODO test
def calculate_snailfish_multiple(sfs: List[Snailfish], debug: bool = False) -> Snailfish:
    current = calculate_snailfish(sfs[0])
    for i, sf in enumerate(sfs):
        if i == 0:
            continue
        if debug:
            print('- current' + current.__str__())
            print('- next: ' + sf.__str__())
        next_r = calculate_snailfish(sf)
        next_l = current
        current = Snailfish()
        current.left = next_l
        current.right = next_r
        current = calculate_snailfish(current, debug)
    return current


def calculate_snailfish(sf: Snailfish, debug: bool = False) -> Snailfish:
    while True:
        if debug:
            print('### before')
            print(sf)
        math_happened = __calc1(sf)
        if not math_happened:
            break
        if debug:
            print('### after')
            print(sf)
            print('###')
    return sf


def __calc1(sf: Snailfish) -> bool:
    if sf.can_explode():
        sf.explode()
        return True

    if sf.can_split():
        sf.split()
        return True
    return False
