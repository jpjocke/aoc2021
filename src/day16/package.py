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

    def type_id(self) -> int:
        return self.package_type_id.as_decimal()

    def value(self) -> int:
        return self.value_binary.as_decimal()

    def is_literal(self):
        return self.type_id() == 4

    def __str__(self):
        return 'v: ' + str(self.version()) + ', t: ' + str(self.type_id())
