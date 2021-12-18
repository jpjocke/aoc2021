import copy
from typing import List

from src.day18.snailfish import Snailfish


def calculate_largest_for_two(sfs: List[Snailfish]) -> int:
    largest = 0
    s1 = copy.deepcopy(sfs)
    s2 = copy.deepcopy(sfs)
    for i, a in enumerate(s1):
        for j, b in enumerate(s2):
            if i == j:
                continue
            ab = Snailfish()
            ab.left = copy.deepcopy(a)
            ab.right = copy.deepcopy(b)
            ab = calculate_snailfish(ab)
            m = ab.magnitude()
            if m > largest:
                largest = m
            ba = Snailfish()
            ba.left = copy.deepcopy(b)
            ba.right = copy.deepcopy(a)
            ba = calculate_snailfish(ba)
            m1 = ba.magnitude()
            if m1 > largest:
                largest = m1

    return largest


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
