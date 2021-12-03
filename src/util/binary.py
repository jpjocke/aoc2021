class Binary:
    value: str

    def __init__(self, value: str):
        self.value = value

    def invert(self):
        value = '';
        for i in range(len(self.value)):
            if self.value[i] == '0':
                value += '1'
            else:
                value += '0'
        self.value = value

    def as_decimal(self) -> int:
        value = 0
        multiplier = 1
        for i in reversed(range(len(self.value))):
            value += int(self.value[i]) * multiplier
            multiplier *= 2
        return value

    def __str__(self):
        return self.value
