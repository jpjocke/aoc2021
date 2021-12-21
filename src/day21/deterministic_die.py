class DeterministicDie:
    __current: int
    rolls: int

    def __init__(self):
        self.__current = 1
        self.rolls = 0

    def next(self) -> int:
        next_value = self.__current
        self.__current += 1
        if self.__current > 100:
            self.__current = 1
        self.rolls += 1
        return next_value
