from src.day18.snailfish import Snailfish


def calculate_snailfish(sf: Snailfish) -> Snailfish:
    while True:
        print('before')
        print(sf)
        math_happened = __calc1(sf)
        if not math_happened:
            break
        print('after')
        print(sf)
    return sf


def __calc1(sf: Snailfish) -> bool:
    if sf.can_explode():
        sf.explode()
        return True

    return False
