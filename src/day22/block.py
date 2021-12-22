from point3D import Point3D


class Block:
    start: Point3D
    end: Point3D

    def volume(self) -> int:
        # include end point in volume
        return (abs(self.start.x - self.end.x) + 1) * (abs(self.start.y - self.end.y) + 1) * (abs(self.start.z - self.end.z) + 1)

    # is self inside other
    def inside(self, other: "Block") -> bool:
        if other.start.x <= self.start.x and other.end.x >= self.end.x:
            if other.start.y <= self.start.y and other.end.y >= self.end.y:
                if other.start.z <= self.start.z and other.end.z >= self.end.z:
                    return True
        return False

    def intersects(self, other: "Block") -> bool:
        if self.__x_intersects(other) and self.__y_intersects(other) and self.__z_intersects(other):
            return True
        return other.__x_intersects(self) and other.__y_intersects(self) and other.__z_intersects(self)

    def __x_intersects(self, other: "Block") -> bool:
        if self.start.x < other.start.x < self.end.x:
            return True
        if self.start.x < other.end.x < self.end.x:
            return True
        return False

    def __y_intersects(self, other: "Block") -> bool:
        if self.start.y < other.start.y < self.end.y:
            return True
        if self.start.y < other.end.y < self.end.y:
            return True
        return False

    def __z_intersects(self, other: "Block") -> bool:
        if self.start.z < other.start.z < self.end.z:
            return True
        if self.start.z < other.end.z < self.end.z:
            return True
        return False

    def __str__(self):
        return self.start.__str__() + '->' + self.end.__str__()
