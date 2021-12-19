import unittest

from binary import Binary
from file_reader import FileReader
from point3D import Point3D


class TestUtil(unittest.TestCase):

    def test_fileReader(self):
        fr = FileReader()
        self.assertEqual("hej", fr.read("../data/file_reader_test1.txt"))

    def test_binary_decimal(self):
        binary = Binary('10110')
        self.assertEqual(22, binary.as_decimal())
        binary2 = Binary('01001')
        self.assertEqual(9, binary2.as_decimal())

    def test_binary_invert(self):
        binary = Binary('10110')
        binary.invert()
        self.assertEqual('01001', binary.value)

    def test_manhattan(self):
        p1 = Point3D(1105, -1205, 1229)
        p2 = Point3D(-92, -2380, -20)
        self.assertEqual(3621, p1.manhattan(p2))
        self.assertEqual(3621, p2.manhattan(p1))


if __name__ == '__main__':
    unittest.main()
