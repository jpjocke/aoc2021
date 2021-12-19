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
        fail_max = 40
        fail = 0
        # last_mapped = 0
        while True:
            mapped = self.__mapped_num()
            # if mapped == last_mapped:
            #    print('no more found exiting')
            #    break
            if fail >= fail_max:
                break
            i += 1
            if i >= len(self.scanners):
                i = 0
                fail += 1
                print('***')
                print('*** failed: ' + str(fail))
                print('*** mapped: ' + str(mapped) + '/' + str(len(self.scanners)))
                print('***')
                if mapped == len(self.scanners):
                    print('*** All found ***')
                    break
                # last_mapped = mapped
            if self.scanners[i].mapped:
                # print(self.scanners[i])
                continue
            self.test_find_diff2(self.scanners[i])
        return len(self.beacons)

    def test_find_diff(self, scanner: Scanner) -> bool:
        print('test: ' + scanner.__str__())
        for scanner_in in self.scanners:
            if not scanner_in.mapped:
                continue
            if scanner_in.id in scanner.no_correlation:
                # print('no cor: ' + str(scanner_in.id))
                continue
            for mutated_list in scanner.b_permutations:
                for mutated in mutated_list:
                    relative = []
                    for b_beacon in scanner_in.b_correct:
                        relative.append(b_beacon.add(scanner_in.pos))
                    for b_beacon in relative:
                        diff = b_beacon.diff(mutated)
                        diff_list = self.__copy_beacons_with_diff(mutated_list, diff)
                        if self.test_diff_list(diff_list):
                            absolute_pos_list = []
                            for b in diff_list:
                                absolute_pos_list.append(b.add(scanner_in.pos))
                            self.beacons.update(absolute_pos_list)
                            scanner.mapped = True
                            scanner.b_correct = mutated_list
                            scanner.pos = diff.add(scanner_in.pos)
                            print('mapped ' + scanner.__str__() + ' with ' + scanner_in.__str__())
                            return True
            # print('no correlation ' + scanner.__str__() + ' -> ' + scanner_in.__str__())
            scanner.no_correlation.append(scanner_in.id)
        return False

    def test_find_diff2(self, scanner: Scanner) -> bool:
        print('test2: ' + scanner.__str__())
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
        # print('hits: ' + str(hits))
        if hits >= 12:
            return True
        return False

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
