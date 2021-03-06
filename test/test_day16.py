import unittest

from src.day16.parse_hex_package import parse_hex_package


class TestDay16(unittest.TestCase):

    def test_problem_1a(self):
        data = 'D2FE28'
        packages = parse_hex_package(data)
        p = packages[0]
        self.assertEqual(p.version(), 6)
        self.assertEqual(p.type_id(), 4)
        self.assertEqual(p.value(), 2021)

    def test_problem_1b(self):
        data = '38006F45291200'
        packages = parse_hex_package(data)
        p = packages[0]
        self.assertEqual(p.version(), 1)
        self.assertEqual(p.type_id(), 6)
        self.assertEqual(len(p.sub_packages), 2)

    def test_problem_1c(self):
        data = 'EE00D40C823060'
        packages = parse_hex_package(data)
        p = packages[0]
        self.assertEqual(p.version(), 7)
        self.assertEqual(p.type_id(), 3)
        self.assertEqual(len(p.sub_packages), 3)

    def test_problem_1d(self):
        data = '8A004A801A8002F478'
        packages = parse_hex_package(data)
        p = packages[0]
        self.assertEqual(p.version_value(), 16)

    def test_problem_1e(self):
        data = '620080001611562C8802118E34'
        packages = parse_hex_package(data)
        p = packages[0]
        self.assertEqual(p.version_value(), 12)

    def test_problem_1f(self):
        data = 'C0015000016115A2E0802F182340'
        packages = parse_hex_package(data)
        p = packages[0]
        self.assertEqual(p.version_value(), 23)

    def test_problem_1g(self):
        data = 'A0016C880162017C3686B18A3D4780'
        packages = parse_hex_package(data)
        p = packages[0]
        self.assertEqual(p.version_value(), 31)

    def test_problem_2a(self):
        data = 'C200B40A82'
        packages = parse_hex_package(data)
        p = packages[0]
        self.assertEqual(p.calculate(), 3)

    def test_problem_2b(self):
        data = '04005AC33890'
        packages = parse_hex_package(data)
        p = packages[0]
        self.assertEqual(p.calculate(), 54)

    def test_problem_2c(self):
        data = '880086C3E88112'
        packages = parse_hex_package(data)
        p = packages[0]
        self.assertEqual(p.calculate(), 7)

    def test_problem_2d(self):
        data = 'CE00C43D881120'
        packages = parse_hex_package(data)
        p = packages[0]
        self.assertEqual(p.calculate(), 9)

    def test_problem_2e(self):
        data = 'D8005AC2A8F0'
        packages = parse_hex_package(data)
        p = packages[0]
        self.assertEqual(p.calculate(), 1)

    def test_problem_2f(self):
        data = 'F600BC2D8F'
        packages = parse_hex_package(data)
        p = packages[0]
        self.assertEqual(p.calculate(), 0)

    def test_problem_2g(self):
        data = '9C005AC2F8F0'
        packages = parse_hex_package(data)
        p = packages[0]
        self.assertEqual(p.calculate(), 0)

if __name__ == '__main__':
    unittest.main()
