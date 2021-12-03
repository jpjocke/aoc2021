import unittest

from binary import Binary
from file_reader import FileReader


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


if __name__ == '__main__':
    unittest.main()
