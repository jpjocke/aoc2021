from math import floor


class Point3D:
    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def diff(self, o: "Point3D") -> "Point3D":
        return Point3D(self.x - o.x, self.y - o.y, self.z - o.z)

    def add(self, o: "Point3D") -> "Point3D":
        return Point3D(self.x + o.x, self.y + o.y, self.z + o.z)

    def manhattan(self, o: "Point3D") -> int:
        return abs(self.x - o.x) + abs(self.y - o.y) + abs(self.z - o.z)

    def __str__(self):
        return 'x: ' + str(self.x) + ', y: ' + str(self.y) + ', z: ' + str(self.z)

    def __eq__(self, other):
        if not isinstance(other, Point3D):
            return NotImplemented

        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        x = self.x
        y = self.y
        z = self.z
        return floor(((x + y) * (x + y + 1) / 2) + y) * floor(((z + y) * (z + y + 1) / 2) + y) * floor(
            ((x + z) * (x + z + 1) / 2) + z)
