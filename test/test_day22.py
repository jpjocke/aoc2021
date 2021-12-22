import unittest

from file_reader import FileReader
from point3D import Point3D
from src.day22.block import Block
from src.day22.reactor import calculate_reactor_volume
from src.day22.reactor_instruction import ReactorInstruction
from src.day22.reactor_naive import calculate_reactor_naive
from src.day22.reactor_parser import parse_reactor


class TestDay22(unittest.TestCase):
    fr = FileReader()

    def test_problem_1(self):
        data = self.fr.read_as_str_lines("../data/day22_test_in.txt")
        instructions = parse_reactor(data)
        result = calculate_reactor_naive(instructions, True)
        self.assertEqual(39, result)

    def test_block_volume(self):
        block = Block()
        block.start = Point3D(-5, -5, -5)
        block.end = Point3D(4, 4, 4)
        self.assertEqual(1000, block.volume())

    def test_block_volume_a(self):
        block = Block()
        block.start = Point3D(10, 10, 10)
        block.end = Point3D(12, 12, 12)
        self.assertEqual(27, block.volume())

    def test_block_intersect(self):
        a = Block()
        a.start = Point3D(1, 1, 1)
        a.end = Point3D(10, 10, 10)
        b = Block()
        b.start = Point3D(2, 8, 8)
        b.end = Point3D(2, 12, 12)
        c = Block()
        c.start = Point3D(6, 8, 8)
        c.end = Point3D(6, 12, 12)
        self.assertTrue(a.intersects(b))
        self.assertTrue(b.intersects(a))
        self.assertTrue(a.intersects(c))
        self.assertFalse(b.intersects(c))

    def test_block_add_no_intersect(self):
        ia = ReactorInstruction()
        ia.on = True
        ia.start = Point3D(10, 10, 10)
        ia.end = Point3D(12, 12, 12)
        ib = ReactorInstruction()
        ib.on = True
        ib.start = Point3D(0, 0, 0)
        ib.end = Point3D(2, 2, 2)
        volume = calculate_reactor_volume([ia, ib])
        # 27 + 27
        self.assertEqual(54, volume)

    def test_block_add_with_intersect_a(self):
        data = self.fr.read_as_str_lines("../data/day22_test_in.txt")
        instructions = parse_reactor(data)
        volume = calculate_reactor_volume([instructions[0], instructions[1]])
        # 27 + 19
        self.assertEqual(46, volume)

    def test_block_add_with_intersect_a_inverse(self):
        data = self.fr.read_as_str_lines("../data/day22_test_in.txt")
        instructions = parse_reactor(data)
        volume = calculate_reactor_volume([instructions[1], instructions[0]])
        # 27 + 19
        self.assertEqual(46, volume)

    def test_block_remove_with_intersect_1(self):
        data = self.fr.read_as_str_lines("../data/day22_test_in.txt")
        instructions = parse_reactor(data)
        instructions[1].on = False
        volume = calculate_reactor_volume([instructions[0], instructions[1]])
        # 27 - 8
        self.assertEqual(19, volume)

    def test_block_remove_with_intersect_2(self):
        data = self.fr.read_as_str_lines("../data/day22_test_in.txt")
        instructions = parse_reactor(data)
        volume = calculate_reactor_volume([instructions[0], instructions[2]])
        # 27 - 8
        self.assertEqual(19, volume)

    def test_problem_2(self):
        data = self.fr.read_as_str_lines("../data/day22_test_in.txt")
        instructions = parse_reactor(data)
        volume = calculate_reactor_volume(instructions)
        # 27 + 19 - 8 + 1
        self.assertEqual(39, volume)

    def test_problem_2a(self):
        data = self.fr.read_as_str_lines("../data/day22a_test_in.txt")
        instructions = parse_reactor(data)
        #volume = calculate_reactor_volume(instructions)
        #self.assertEqual(2758514936282235, volume)

    def test_problem_2b(self):
        # det finns nog fler remove fall...
        # inside
        # inside one side
        # hole
        data = self.fr.read_as_str_lines("../data/day22b_test_in.txt")
        instructions = parse_reactor(data)
        volume = calculate_reactor_volume(instructions)
        self.assertEqual(588200, volume)

if __name__ == '__main__':
    unittest.main()
