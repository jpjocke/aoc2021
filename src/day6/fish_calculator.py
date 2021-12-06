from typing import List


def next_day(data: List[int]) -> List[int]:
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


def get_iterate_9_map() -> {}:
    iterate_map = {}
    for i in range(9):
        fish = [i]
        for y in range(9):
            fish = next_day(fish)
        iterate_map[i] = fish

    return iterate_map


class FishCalculator:
    sum_map: {}
    iterate_9_map: {}

    def __init__(self):
        self.sum_map = {}
        self.iterate_9_map = get_iterate_9_map()

    def calc(self, data: List[int], iterations: int) -> int:
        # make the total itetions dividable by 9 since we are using steps of 9
        while iterations % 9 != 0:
            data = next_day(data)
            iterations -= 1

        total = 0
        for fish in data:
            total += self.__calc_single(fish, iterations)

        # for key in self.sum_map:
        #    print(key + ' -> ' + str(self.sum_map[key]))
        return total

    # recursive, checks the value for one single fish and the amount of iterations left for it
    def __calc_single(self, value: int, iterations: int) -> int:
        key = self.__get_key(iterations, value)
        if key in self.sum_map:
            # print('HIT: ' + key + ': ' + str(self.sum_map[key]))
            return self.sum_map[key]
        if iterations == 0:
            return 1
        next_fish = self.iterate_9_map[value]
        total = 0
        for fish in next_fish:
            total += self.__calc_single(fish, iterations - 9)
        # print('PUT: ' + key + ': ' + str(total))
        self.sum_map[key] = total
        return total

    def __get_key(self, iterations: int, value: int) -> str:
        return str(iterations) + '-' + str(value)
