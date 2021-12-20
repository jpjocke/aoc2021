import unittest

from src.day20.image_parser import parse_image
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_problem_1(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day20_test_in.txt")
        image = parse_image(data)
        print(image)
        print('---')
        image.enhance()
        print(image)
        image.enhance()
        print(image)
        self.assertEqual(35, image.count())

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day20_test_in.txt")
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
