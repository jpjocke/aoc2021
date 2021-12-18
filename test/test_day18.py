import unittest

from day18.snailfish_math import calculate_snailfish
from day18.snailfish_parser import parse_snailfish
from file_reader import FileReader


class TestDayThree(unittest.TestCase):

    def test_parse_1(self):
        data = ['[[1,2],3]']
        sf = parse_snailfish(data)[0]
        self.assertEqual(sf.right, 3)
        self.assertEqual(sf.left.left, 1)
        self.assertEqual(sf.left.right, 2)

    def test_parse_1a(self):
        data = ['[9,[8,7]]']
        sf = parse_snailfish(data)[0]
        self.assertEqual(sf.left, 9)
        self.assertEqual(sf.right.left, 8)
        self.assertEqual(sf.right.right, 7)

    def test_parse_1b(self):
        data = ['[[1,9],[8,5]]']
        sf = parse_snailfish(data)[0]
        self.assertEqual(sf.left.left, 1)
        self.assertEqual(sf.left.right, 9)
        self.assertEqual(sf.right.left, 8)
        self.assertEqual(sf.right.right, 5)

    def test_parse_1c(self):
        data = ['[[[[1,2],[3,4]],[[5,6],[7,8]]],9]']
        sf = parse_snailfish(data)[0]
        self.assertEqual(sf.right, 9)
        self.assertEqual(sf.left.left.left.left, 1)
        self.assertEqual(sf.left.left.left.right, 2)
        self.assertEqual(sf.left.left.right.right, 4)

    def test_depth_1(self):
        data = ['[[[[1,2],[3,4]],[[5,6],[7,8]]],9]']
        sf = parse_snailfish(data)[0]
        self.assertEqual(sf.depth(), 3)
        self.assertEqual(sf.left.depth(), 2)

    def test_explode_left(self):
        print('explode left')
        data = ['[[[[[9,8],1],2],3],4]']
        sf = parse_snailfish(data)[0]
        self.assertEqual(sf.depth(), 4)
        sf = calculate_snailfish(sf)
        self.assertEqual(sf.depth(), 3)
        self.assertEqual(sf.left.left.left.left, 0)
        self.assertEqual(sf.left.left.left.right, 9)
        self.assertEqual(sf.left.left.right, 2)

    def test_explode_right(self):
        print('explode right')
        data = ['[7,[6,[5,[4,[3,2]]]]]']
        sf = parse_snailfish(data)[0]
        self.assertEqual(sf.depth(), 4)
        sf = calculate_snailfish(sf)
        self.assertEqual(sf.depth(), 3)
        self.assertEqual(sf.right.right.right.right, 0)
        self.assertEqual(sf.right.right.right.left, 7)

    def test_explode_middle(self):
        print('explode middle')
        data = ['[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]']
        sf = parse_snailfish(data)[0]
        self.assertEqual(sf.depth(), 4)
        sf = calculate_snailfish(sf)
        self.assertEqual(sf.depth(), 3)
        self.assertEqual(sf.right.left, 9)
        self.assertEqual(sf.right.right.right.left, 7)
        self.assertEqual(sf.right.right.right.right, 0)
        self.assertEqual(sf.left.right.right.left, 8)
        self.assertEqual(sf.left.right.right.right, 0)

    def test_problem_2(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day18_test_in.txt")
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
