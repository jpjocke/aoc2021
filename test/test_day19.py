import unittest

from point3D import Point3D
from src.day19.scanner import Scanner
from src.day19.beacon_map import BeaconMap
from src.day19.scanner_parser import parse_scanners
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day19_test_in.txt")
        scanners = parse_scanners(data)
        beacon_map = BeaconMap(scanners)
        count = beacon_map.calculate_map()

        self.assertEqual(79, count)
        self.assertEqual(3621, beacon_map.longest_manhattan())

    def test_problem_1a_small(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day19a_test_in.txt")
        scanners = parse_scanners(data)
        beacon_map = BeaconMap(scanners)
        count = beacon_map.calculate_map()

        self.assertEqual(13, count)

    def test_problem_1a(self):
        s1, s2 = self.__create_test_scanners()
        beacon_map = BeaconMap([s1, s2])
        count = beacon_map.calculate_map()
        # for a in s1.b_permutations:
        #    print(a[2])

        # beacons is 12 + 13, needed to be able to map.
        # result is 4 because the set strips away all the ones that are identical
        self.assertEqual(4, count)

    def __create_test_scanners(self) -> (Scanner, Scanner):
        s1 = Scanner(0)
        s1.add_beacon(Point3D(1, 1, 1))
        s1.add_beacon(Point3D(3, 5, 2))
        s1.add_beacon(Point3D(5, 6, -4))
        s1.add_beacon(Point3D(3, 5, 2))
        s1.add_beacon(Point3D(3, 5, 2))
        s1.add_beacon(Point3D(3, 5, 2))
        s1.add_beacon(Point3D(3, 5, 2))
        s1.add_beacon(Point3D(3, 5, 2))
        s1.add_beacon(Point3D(3, 5, 2))
        s1.add_beacon(Point3D(3, 5, 2))
        s1.add_beacon(Point3D(3, 5, 2))
        s1.add_beacon(Point3D(3, 5, 2))
        s2 = Scanner(1)
        s2.add_beacon(Point3D(-1, -1, -1))
        s2.add_beacon(Point3D(1, 3, 0))
        s2.add_beacon(Point3D(3, 4, -6))
        s2.add_beacon(Point3D(1, 3, 0))
        s2.add_beacon(Point3D(1, 3, 0))
        s2.add_beacon(Point3D(1, 3, 0))
        s2.add_beacon(Point3D(1, 3, 0))
        s2.add_beacon(Point3D(1, 3, 0))
        s2.add_beacon(Point3D(1, 3, 0))
        s2.add_beacon(Point3D(1, 3, 0))
        s2.add_beacon(Point3D(1, 3, 0))
        s2.add_beacon(Point3D(1, 3, 0))
        s2.add_beacon(Point3D(10, 30, 3))
        return s1, s2

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day19_test_in.txt")
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
