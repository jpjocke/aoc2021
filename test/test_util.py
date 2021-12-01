import unittest

from file_reader import FileReader


class TestUtil(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_fileReader(self):
        fr = FileReader()
        self.assertEqual(fr.read("../data/file_reader_test1.txt"), "hej")


if __name__ == '__main__':
    unittest.main()
