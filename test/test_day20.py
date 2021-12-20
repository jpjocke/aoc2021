import unittest

from src.day20.image_parser import parse_image
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day20_test_in.txt")
        image = parse_image(data)
        image.enhance()
        image.enhance()
        self.assertEqual(35, image.count())

    def test_problem_1a(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day20a_test_in.txt")
        image = parse_image(data)
        image.enhance()
        image.enhance()
        self.assertEqual(5326, image.count())

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day20_test_in.txt")
        image = parse_image(data)
        for i in range(50):
            image.enhance()
        self.assertEqual(3351, image.count())


if __name__ == '__main__':
    unittest.main()
