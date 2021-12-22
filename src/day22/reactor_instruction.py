from point3D import Point3D


class ReactorInstruction:
    on: bool
    start: Point3D
    end: Point3D

    def __str__(self):
        sb = 'on' if self.on else 'off'
        return sb + ': [' + self.start.__str__() + '],[' + self.end.__str__() + ']'
