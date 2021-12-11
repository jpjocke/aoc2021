import unittest

from src.day11.dumbo_map import DumboMap
from src.day11.dumbo_parser import parse_dumbos
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day11_test_in.txt")
        dumbos = parse_dumbos(data)
        dumbo_map = DumboMap(dumbos)
        for i in range(100):
            dumbo_map.simulate_one()
        print(dumbo_map)
        flashes = dumbo_map.count_flashes()
        self.assertEqual(flashes, 1656)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day11_test_in.txt")
        dumbos = parse_dumbos(data)
        dumbo_map = DumboMap(dumbos)
        sims = 0
        synced = False
        while not synced:
            sims += 1
            synced = dumbo_map.simulate_one()
            print(dumbo_map)
        self.assertEqual(sims, 195)


if __name__ == '__main__':
    unittest.main()
