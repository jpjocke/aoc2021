from typing import List

from binary import Binary


class Package:
    package_version: Binary
    package_type_id: Binary
    value_binary: Binary
    sub_packages: List["Package"]

    def __init__(self):
        self.sub_packages = []

    def version(self) -> int:
        return self.package_version.as_decimal()

    def version_value(self) -> int:
        value = self.version()
        for sub in self.sub_packages:
            value += sub.version_value()
        return value

    def calculate(self) -> int:
        if self.type_id() == 0:  # sum
            value = 0
            for sub in self.sub_packages:
                value += sub.calculate()
            return value
        if self.type_id() == 1:  # product
            value = 1
            for sub in self.sub_packages:
                value *= sub.calculate()
            return value
        if self.type_id() == 2:  # min
            value = 99999999999999999999
            for sub in self.sub_packages:
                v = sub.calculate()
                if v < value:
                    value = v
            return value
        if self.type_id() == 3:  # max
            value = 0
            for sub in self.sub_packages:
                v = sub.calculate()
                if v > value:
                    value = v
            return value

        if self.type_id() == 4:  # literal
            return self.value()

        if self.type_id() == 5:  # gt
            if self.sub_packages[0].calculate() > self.sub_packages[1].calculate():
                return 1
            else:
                return 0

        if self.type_id() == 6:  # lt
            if self.sub_packages[0].calculate() < self.sub_packages[1].calculate():
                return 1
            else:
                return 0

        if self.type_id() == 7:  # eq
            if self.sub_packages[0].calculate() == self.sub_packages[1].calculate():
                return 1
            else:
                return 0

    def type_id(self) -> int:
        return self.package_type_id.as_decimal()

    def value(self) -> int:
        return self.value_binary.as_decimal()

    def is_literal(self):
        return self.type_id() == 4

    def __str__(self):
        return 'v: ' + str(self.version()) + ', t: ' + str(self.type_id())
