import copy
from collections import defaultdict
from typing import List, Tuple

from point import Point
from src.day23.amphipod import Amphipod
from src.day23.hallway import Hallway


class HallwaySolver:
    shortest_distance: int
    snapshots: List[str]
    depths: {int, int}
    depths_print: int

    def __init__(self):
        self.shortest_distance = 9999999999
        self.snapshots = []
        self.depths = defaultdict(int)
        self.depths_print = 0

    def solve(self, hallway: Hallway) -> int:
        self.__solve(hallway, 0, 0)
        return self.shortest_distance

    def __solve(self, hallway: Hallway, total_cost: int, iterations: int):
        snapshot = hallway.snapshot() + str(total_cost)
        if snapshot in self.snapshots:
            return
        self.snapshots.append(snapshot)
        if iterations > 40:
            return
        if total_cost > self.shortest_distance:
            return
        if hallway.is_solved():
            print('found end: ' + str(total_cost))
            if total_cost < self.shortest_distance:
                self.shortest_distance = total_cost
            return
        moves: List[Tuple[Amphipod, Point, int]] = hallway.possible_moves()
        if len(moves) == 0:
            return
        self.depths[iterations] += len(moves)
        for amphi, pos, cost in moves:
            hallway_inner = copy.deepcopy(hallway)
            hallway_inner.move_amphi(amphi, pos)

            self.print_depth()
            self.__solve(hallway_inner, total_cost + cost, iterations + 1)
            self.depths[iterations] -= 1

    def print_depth(self):
        self.depths_print += 1
        if self.depths_print != 20000:
            return
        self.depths_print = 0
        sb = ''
        for key in self.depths:
            sb += str(self.depths[key]) + '-'
        print(sb)
