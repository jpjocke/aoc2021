import unittest

from day18.snailfish_math import calculate_snailfish, calculate_snailfish_multiple
from day18.snailfish_parser import parse_snailfish
from file_reader import FileReader


class TestDay18(unittest.TestCase):

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
        self.assertEqual(data[0], sf.__str__())

    def test_parse_dd_1(self):
        data = ['[[[[10,12],[3,4]],[[5,6],[7,8]]],9]']
        sf = parse_snailfish(data)[0]
        self.assertEqual(data[0], sf.__str__())

    def test_depth_1(self):
        data = ['[[[[1,2],[3,4]],[[5,6],[7,8]]],9]']
        sf = parse_snailfish(data)[0]
        self.assertEqual(sf.depth(), 3)
        self.assertEqual(sf.left.depth(), 2)

    def test_explode_left(self):
        data = ['[[[[[9,8],1],2],3],4]']
        sf = parse_snailfish(data)[0]
        self.assertEqual(sf.depth(), 4)
        sf = calculate_snailfish(sf)
        self.assertEqual(sf.depth(), 3)
        self.assertEqual(sf.left.left.left.left, 0)
        self.assertEqual(sf.left.left.left.right, 9)
        self.assertEqual(sf.left.left.right, 2)

    def test_explode_right(self):
        data = ['[7,[6,[5,[4,[3,2]]]]]']
        sf = parse_snailfish(data)[0]
        self.assertEqual(sf.depth(), 4)
        sf = calculate_snailfish(sf)
        self.assertEqual(sf.depth(), 3)
        self.assertEqual(sf.right.right.right.right, 0)
        self.assertEqual(sf.right.right.right.left, 7)
        self.assertEqual(sf.__str__(), '[7,[6,[5,[7,0]]]]')

    def test_explode_middle(self):
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
        self.assertEqual(sf.__str__(), '[[3,[2,[8,0]]],[9,[5,[7,0]]]]')

    def test_split(self):
        data = ['[[[[0,7],4],[15,[0,13]]],[1,1]]']
        sf = parse_snailfish(data)[0]
        sf = calculate_snailfish(sf)
        self.assertEqual(sf.__str__(), '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')

    def test_problem_1_multiple_lines(self):
        data = ['[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]']
        sfs = parse_snailfish(data)
        sf = calculate_snailfish_multiple(sfs)
        self.assertEqual(sf.__str__(), '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')

    def test_problem_1a_multiple_lines(self):
        data = ['[1,1]', '[2,2]', '[3,3]', '[4,4]']
        sfs = parse_snailfish(data)
        sf = calculate_snailfish_multiple(sfs)
        self.assertEqual(sf.__str__(), '[[[[1,1],[2,2]],[3,3]],[4,4]]')

    def test_problem_1c_multiple_lines(self):
        fr = FileReader()
        data = fr.read_as_str_lines("../data/day18_test_in.txt")
        sfs = parse_snailfish(data)
        sf = calculate_snailfish_multiple(sfs, True)
        self.assertEqual(sf.__str__(), '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')


if __name__ == '__main__':
    unittest.main()
