from typing import List, Set

from point3D import Point3D
from src.day19.scanner import Scanner


class BeaconMap:
    scanners: List[Scanner]
    beacons: Set[Point3D]

    def __init__(self, scanners: List[Scanner]):
        self.scanners = scanners
        self.beacons = set(scanners[0].b_raw)
        self.scanners[0].mapped = True
        self.scanners[0].b_correct = self.scanners[0].b_raw

    def calculate_map(self) -> int:
        i = -1
        iterations = 0
        while True:
            i += 1
            if i >= len(self.scanners):
                i = 0
                iterations += 1
                mapped = self.__mapped_num()
                print('***')
                print('*** iterations: ' + str(iterations))
                print('*** mapped: ' + str(mapped) + '/' + str(len(self.scanners)))
                print('***')
                if mapped == len(self.scanners):
                    print('*** All found ***')
                    break
            if self.scanners[i].mapped:
                continue
            self.test_find_diff2(self.scanners[i])
        return len(self.beacons)

    def test_find_diff2(self, scanner: Scanner) -> bool:
        print('testing: ' + scanner.__str__())
        for mutated_list in scanner.b_permutations:
            for mutated in mutated_list:
                for b_beacon in self.beacons:
                    diff_to_zero = b_beacon.diff(mutated)
                    orig_zero_list = self.__copy_beacons_with_diff(mutated_list, diff_to_zero)
                    if self.test_diff_list(orig_zero_list):
                        self.beacons.update(orig_zero_list)
                        scanner.mapped = True
                        scanner.pos = diff_to_zero
                        print('mapped ' + scanner.__str__())
                        print('beacons: ' + str(len(self.beacons)))
                        return True

        return False

    def test_diff_list(self, diff_list: List[Point3D]) -> bool:
        hits = 0
        for b in diff_list:
            if b in self.beacons:
                hits += 1
        if hits >= 12:
            return True
        return False

    def longest_manhattan(self) -> int:
        a = [*map(lambda scanner: scanner.pos, self.scanners)]
        b = [*map(lambda scanner: scanner.pos, self.scanners)]
        longest = 0
        for x in a:
            for y in b:
                # print(x.__str__() + ' : ' + y.__str__())
                distance = x.manhattan(y)
                if distance > longest:
                    longest = distance
        return longest

    def __mapped_num(self) -> int:
        total = 0
        for s in self.scanners:
            if s.mapped:
                total += 1
        return total

    def __copy_beacons_with_diff(self, beacons: List[Point3D], diff: Point3D) -> List[Point3D]:
        copy_list = []
        for b in beacons:
            copy_list.append(b.add(diff))
        return copy_list
