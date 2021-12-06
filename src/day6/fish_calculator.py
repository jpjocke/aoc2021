from typing import List

def __next(data: List[int]) -> List[int]:
    next_data = []
    next_fish = []
    for i in data:
        i -= 1
        if i == -1:
            i = 6
            next_fish.append(8)
        next_data.append(i)
    next_data.extend(next_fish)
    return next_data

def calculate_fish(data: List[int], iterations: int) -> List[int]:
    a = 0
    while iterations > 0:
        data = __next(data)
        iterations -= 1
        a += 1
        print(iterations)
        print(data)
    return data