import unittest

from binary import Binary
from file_reader import FileReader


class TestUtil(unittest.TestCase):

    def test_fileReader(self):
        fr = FileReader()
        self.assertEqual(fr.read("../data/file_reader_test1.txt"), "hej")

    def test_binary_decimal(self):
        binary = Binary('10110')
        self.assertEqual(binary.as_decimal(), 22)
        binary.invert()
        self.assertEqual(binary.value, '01001')
        binary2 = Binary('01001')
        self.assertEqual(binary2.as_decimal(), 9)


if __name__ == '__main__':
    unittest.main()
