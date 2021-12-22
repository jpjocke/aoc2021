from point3D import Point3D
from src.day22.block import Block


class ReactorInstruction:
    on: bool
    start: Point3D
    end: Point3D

    def get_block(self) -> Block:
        block = Block()
        block.start = self.start
        block.end = self.end
        return block

    def __str__(self):
        sb = 'on' if self.on else 'off'
        return sb + ': [' + self.start.__str__() + '],[' + self.end.__str__() + ']'
