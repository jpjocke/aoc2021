from typing import List

from binary import Binary
from hex import Hex
from src.day16.package import Package


def parse_hex_package(hex: str) -> List[Package]:
    print('hex: ' + hex)
    full_package = ''
    hex_parse = Hex()
    for l in hex:
        full_package += hex_parse.to_binary(l).value
    return __parse_packages(full_package)


def __parse_packages(data: str) -> List[Package]:
    packages = []
    p, _ = __parse_package(data)
    packages.append(p)
    return packages


def __parse_package(data: str) -> (Package, int):
    package = Package()
    package.package_version = Binary(data[0:3])
    package.package_type_id = Binary(data[3:6])
    index = 6
    if package.is_literal():
        index = __parse_literal_value(data, index, package)
    else:
        if data[6] == '0':
            index = 7 + 15
            length = Binary(data[7:index])
            end = index + length.as_decimal()
            sub = data[index:end]
            inner_length = 0
            while inner_length < length.as_decimal():
                p, i = __parse_package(sub)
                package.sub_packages.append(p)
                sub = sub[i::]
                inner_length += i
            index = end
        else:
            index = 7 + 11
            numbers = Binary(data[7:index])
            sub = data[index::]
            while len(package.sub_packages) < numbers.as_decimal():
                p, i = __parse_package(sub)
                package.sub_packages.append(p)
                sub = sub[i::]
                index += i

    return package, index


def __parse_literal_value(data: str, index: int, package: Package) -> int:
    sb = ''
    while True:
        sb += data[index + 1:index + 5]
        if data[index] == '1':
            index += 5
        else:
            break

    index += 5
    # while index < len(data) and data[index] == '0':
    #    index += 1
    package.value_binary = Binary(sb)
    return index  # not correct?
