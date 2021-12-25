from typing import List, Union, Tuple

from src.day24.op import Operator, OpIn


class ALU:
    w: int
    x: int
    y: int
    z: int
    operators: List[Operator]
    input: List[int]
    __input_order: int
    __cache: {str, Tuple[int, int, int, int]}
    __input_places: List[int]

    def __init__(self):
        self.reset()
        self.operators = []
        self.__cache = {}
        self.__input_places = []

    def add_operator(self, op: Operator):
        if isinstance(op, OpIn):
            self.__input_places.append(len(self.operators))
        self.operators.append(op)

    def add_input(self, value: int):
        self.input.append(value)
        # mark input index

    def add_input_list(self, values: List[int]):
        self.input = values
        # mark input indexes

    def reset(self):
        self.input = []
        self.__input_order = 0
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0

    def run(self, debug=False):
        if debug:
            print('-- RUNNING --')
        cache_used = False
        previous_state = self.__state()
        i = 0
        while i < len(self.operators):
        # for op in self.operators:
            op = self.operators[i]
            if debug:
                print(op)
            if isinstance(op, OpIn):
                # store cache for previous calc
                if self.__input_order > 0 and not cache_used:
                    previous_key = self.__snapshot_with_state(self.__input_order - 1, previous_state)
                    if previous_key not in self.__cache:
                        if debug:
                            print('### store cache: ' + previous_key)
                        self.__cache[previous_key] = self.__state()
                cache_used = False
                previous_state = self.__state()

                # check cache for this calc
                this_key = self.__snapshot_with_state(self.__input_order, self.__state())
                if this_key in self.__cache:
                    if debug:
                        print('### cache hit: ' + this_key + " -> " + str(self.__cache[this_key]))
                    cache = self.__cache[this_key]
                    self.w = cache[0]
                    self.x = cache[1]
                    self.y = cache[2]
                    self.z = cache[3]
                    cache_used = True
                    self.__input_order += 1
                    i = self.__input_places[self.__input_order]
                    continue
                value = op.input(self.input, self.__input_order)
                self.__input_order += 1
                self.__store(value, op.a)
                if debug:
                    print('store ' + str(value) + ' in ' + op.a)
                i += 1
            elif cache_used:
                i += 1
                continue
            else:
                a = self.__take(op.a)
                b = self.__take(op.b)
                value = op.run(a, b)
                self.__store(value, op.a)
                i += 1
                if debug:
                    print(str(a) + ' | ' + str(b))
                    print('store result ' + str(value) + ' in ' + op.a)

    def __store(self, value: int, place: str):
        if place == 'w':
            self.w = value
        elif place == 'x':
            self.x = value
        elif place == 'y':
            self.y = value
        elif place == 'z':
            self.z = value

    def __take(self, place: Union[str, int]) -> int:
        if isinstance(place, int):
            return place
        if place == 'w':
            return self.w
        elif place == 'x':
            return self.x
        elif place == 'y':
            return self.y
        elif place == 'z':
            return self.z

    def __state(self) -> Tuple[int, int, int, int]:
        return self.w, self.x, self.y, self.z

    def __snapshot_with_state(self, input_order: int, state: Tuple[int, int, int, int]) -> str:
        return str(state[0]) + '-' + str(state[1]) + '-' + str(state[2]) + '-' + str(state[3]) + '-' + str(
            input_order) + '-' + str(self.input[input_order])
