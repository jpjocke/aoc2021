from typing import List

from point3D import Point3D


class Scanner:
    id: int
    pos: Point3D
    mapped: bool
    no_correlation: List[int]
    b_raw: List[Point3D]
    b_correct: List[Point3D]
    b_permutations: List[List[Point3D]]

    def __init__(self, id: int):
        self.id = id
        self.b_raw = []
        self.b_permutations = []
        self.no_correlation = []
        for i in range(48):
            self.b_permutations.append([])
        self.mapped = False

    def add_beacon(self, beacon: Point3D):
        self.b_raw.append(beacon)
        self.__mutate(beacon)

    def __mutate(self, beacon: Point3D):
        x = beacon.x
        y = beacon.y
        z = beacon.z
        mutated = self.__mutate_xyz(x, y, z)
        mutated += self.__mutate_xyz(x, z, y)
        mutated += self.__mutate_xyz(y, x, z)
        mutated += self.__mutate_xyz(y, z, x)
        mutated += self.__mutate_xyz(z, y, x)
        mutated += self.__mutate_xyz(z, x, y)
        for i, mut in enumerate(mutated):
            self.b_permutations[i].append(mut)

    def __mutate_xyz(self, x: int, y: int, z: int) -> List[Point3D]:
        mutated = []
        mutated.append(Point3D(x, y, z))
        mutated.append(Point3D(x, y, -z))
        mutated.append(Point3D(x, -y, z))
        mutated.append(Point3D(x, -y, -z))
        mutated.append(Point3D(-x, -y, z))
        mutated.append(Point3D(-x, -y, -z))
        mutated.append(Point3D(-x, y, z))
        mutated.append(Point3D(-x, y, -z))
        return mutated

    def __str__(self):
        sb = str(self.id) + ': '
        if self.mapped:
            sb += self.pos.__str__() + '-(M)'
        else:
            sb += 'Not mapped'
        return sb
