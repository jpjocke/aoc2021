from typing import List, Tuple

from point import Point
from src.day23.amphipod import Amphipod


class Hallway:
    pos_map: {Point, Amphipod}

    def __init__(self):
        self.pos_map = {}

    def add_amphipod(self, amphipod: Amphipod):
        self.pos_map[amphipod.pos] = amphipod

    def is_solved(self) -> bool:
        for key in self.pos_map:
            if not self.pos_map[key].is_in_end_lane():
                return False
        return True

    def move_amphi(self, amphi: Amphipod, pos: Point):
        inner_amphi = self.pos_map[amphi.pos]
        del self.pos_map[amphi.pos]
        inner_amphi.pos = pos
        self.pos_map[pos] = inner_amphi

    def possible_moves(self) -> List[Tuple[Amphipod, Point, int]]:
        moves = []
        for key in self.pos_map:
            amphi: Amphipod = self.pos_map[key]
            if self.__is_in_end_pos(amphi):
                continue
            if self.__blocked_in_room(amphi):
                continue
            possible = self.__remove_occupied_places(amphi)
            possible = self.__run_position_rules(amphi, possible)
            for position in possible:
                moves.append((amphi, position, amphi.cost_to(position)))
        return moves

    def __blocked_in_room(self, amphi: Amphipod) -> bool:
        return Point(amphi.pos.x, amphi.pos.y - 1) in self.pos_map

    def __in_end_pos(self, amphi: Amphipod) -> bool:
        if amphi.is_in_end_lane():
            if amphi.pos.y == 5:
                return True
            if self.__in_end_pos(self.pos_map[Point(amphi.pos.x, amphi.pos.y + 1)]):
                return True
        return False

    def __remove_occupied_places(self, amphi: Amphipod) -> List[Point]:
        allowed = amphi.allowed_pos()
        possible = []
        for pos in allowed:
            if pos not in self.pos_map:
                possible.append(pos)
        return possible

    def __run_position_rules(self, amphi: Amphipod, positions: List[Point]) -> List[Point]:
        possible = []

        orig_pos = amphi.pos
        for position in positions:
            if self.__is_corridor_blocked(orig_pos, position):
                continue
            # only go into rooms with same type
            if position.y != 1 and not self.__is_room_x_of_same_type(position.x, amphi.type):
                continue
            if position.y != 1 and self.__is_room_x_of_same_type(position.x, amphi.type):
                if position.y == 5:
                    # this is the end place
                    return [position]
                # always go deepest into rooms
                if Point(position.x, position.y + 1) not in self.pos_map:
                    continue
                if Point(position.x, position.y + 1) in self.pos_map:
                    # this is the end place
                    return [position]
            possible.append(position)

        return possible

    def __is_corridor_blocked(self, orig_pos: Point, next_pos: Point):
        # is 2,1 blocking?
        if self.__is_x_1_blocking(2, orig_pos, next_pos):
            return True
        # is 4,1 blocking?
        if self.__is_x_1_blocking(4, orig_pos, next_pos):
            return True
        # is 6,1 blocking?
        if self.__is_x_1_blocking(6, orig_pos, next_pos):
            return True
        # is 8,1 blocking?
        if self.__is_x_1_blocking(8, orig_pos, next_pos):
            return True
        # is 10,1 blocking?
        if self.__is_x_1_blocking(10, orig_pos, next_pos):
            return True
        return False

    def __is_x_1_blocking(self, x: int, orig_pos: Point, next_pos: Point) -> bool:
        if Point(x, 1) in self.pos_map:
            if orig_pos.x < x < next_pos.x:
                return True
            if orig_pos.x > x > next_pos.x:
                return True
        return False

    def __is_room_x_of_same_type(self, x: int, type: str):
        for y in range(2, 6):
            p = Point(x, y)
            if p in self.pos_map:
                if self.pos_map[p].type != type:
                    return False
        return True

    def __is_in_end_pos(self, amphi: Amphipod):
        if amphi.is_in_end_lane():
            return self.__is_room_x_of_same_type(amphi.pos.x, amphi.type)

    def snapshot(self) -> str:
        sb = ''
        for y in range(7):
            for x in range(13):
                key = Point(x, y)
                if key in self.pos_map:
                    sb += self.pos_map[key].type + self.pos_map[key].pos.__str__()
        return sb

    def __str__(self):
        sb = ''
        for y in range(7):
            for x in range(13):
                key = Point(x, y)
                if key in self.pos_map:
                    sb += self.pos_map[key].type
                elif y == 0 or y == 6:
                    sb += '#'
                elif x == 0 or x == 12:
                    sb += '#'
                elif y > 1 and (x == 1 or x == 2 or x == 4 or x == 6 or x == 8 or x == 10 or x == 11):
                    sb += '#'
                else:
                    sb += '.'
            sb += '\n'
        return sb
