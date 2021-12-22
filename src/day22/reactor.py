import copy
from typing import List

from src.day22.block import Block
from src.day22.reactor_instruction import ReactorInstruction


def calculate_reactor_volume(instructions: List[ReactorInstruction]) -> int:
    blocks = [instructions[0].get_block()]
    for i, instruction in enumerate(instructions):
        if i == 0:
            continue
        block = instruction.get_block()
        if block.volume() == 0:
            continue
        print(instruction)
        if instruction.on:
            blocks = __run_add(blocks, block)
        else:
            blocks = __run_remove(blocks, block)

    volume = 0
    for block in blocks:
        volume += block.volume()
    return volume


def __run_add(blocks: List[Block], add_block: Block) -> List[Block]:
    i_blocks = [add_block]
    for block in blocks:
        next_blocks = copy.deepcopy(i_blocks)
        i_blocks = []
        for i_block in next_blocks:
            if block.intersects(i_block):
                union = []
                __union(block, i_block, union)
                i_blocks += union
            else:
                i_blocks.append(i_block)
    blocks += i_blocks
    return blocks


def __union(block1: Block, block2: Block, blocks: List[Block]):
    if block2.start.x < block1.start.x:
        x = block1.start.x
        blocks.append(__copy_for_x(block2, x - 1, False))
        block2.start.x = x
        __union(block1, block2, blocks)
    elif block2.end.x > block1.end.x:
        x = block1.end.x
        blocks.append(__copy_for_x(block2, x + 1, True)) # rätt
        block2.end.x = x
        __union(block1, block2, blocks)
    elif block2.start.y < block1.start.y:
        y = block1.start.y
        blocks.append(__copy_for_y(block2, y - 1, False))
        block2.start.y = y
        __union(block1, block2, blocks)
    elif block2.end.y > block1.end.y:
        y = block1.end.y
        blocks.append(__copy_for_y(block2, y + 1, True))
        block2.end.y = y
        __union(block1, block2, blocks)
    elif block2.start.z < block1.start.z:
        z = block1.start.z
        blocks.append(__copy_for_z(block2, z - 1, False))
        block2.start.z = z
        __union(block1, block2, blocks)
    elif block2.end.z > block1.end.z:
        z = block1.end.z
        blocks.append(__copy_for_z(block2, z + 1, True))
        block2.end.z = z
        __union(block1, block2, blocks)


def __copy_for_x(block2, x, start: bool):
    a = Block()
    a.start = copy.deepcopy(block2.start)
    a.end = copy.deepcopy(block2.end)
    if start:
        a.start.x = x
    else:
        a.end.x = x
    return a


def __copy_for_y(block2, y, start: bool):
    a = Block()
    a.start = copy.deepcopy(block2.start)
    a.end = copy.deepcopy(block2.end)
    if start:
        a.start.y = y
    else:
        a.end.y = y
    return a


def __copy_for_z(block2, z, start: bool):
    a = Block()
    a.start = copy.deepcopy(block2.start)
    a.end = copy.deepcopy(block2.end)
    if start:
        a.start.z = z
    else:
        a.end.z = z
    return a


def __run_remove(blocks: List[Block], remove_block: Block) -> List[Block]:
    i_blocks = []
    for block in blocks:
        if block.intersects(remove_block):
            new_blocks = []
            __diff(block, remove_block, new_blocks)
            i_blocks += new_blocks
    blocks += i_blocks
    return blocks


def __diff(keep: Block, remove: Block, blocks: List[Block]):
    # insluten?
    if keep.start.x < remove.end.x < keep.end.x:
        x = remove.end.x
        a = __copy_for_x(keep, x, False)
        keep.start.x = x + 1
        if not a.inside(remove):
            blocks.append(a)
            __diff(a, remove, blocks)
    elif keep.start.x < remove.start.x < keep.end.x:
        x = remove.start.x
        a = __copy_for_x(keep, x, True)
        keep.end.x = x - 1
        if not a.inside(remove):
            blocks.append(a)
            __diff(a, remove, blocks)
    elif keep.start.y < remove.end.y < keep.end.y:
        y = remove.end.y
        a = __copy_for_y(keep, y, False)
        keep.start.y = y + 1
        if not a.inside(remove):
            blocks.append(a)
            __diff(a, remove, blocks)
    elif keep.start.y < remove.start.y < keep.end.y:
        y = remove.start.y
        a = __copy_for_y(keep, y, True)
        keep.end.y = y - 1
        if not a.inside(remove):
            blocks.append(a)
            __diff(a, remove, blocks)
    elif keep.start.z < remove.end.z < keep.end.z:
        z = remove.end.z
        a = __copy_for_z(keep, z, False)
        keep.start.z = z + 1
        if not a.inside(remove):
            blocks.append(a)
            __diff(a, remove, blocks)
    elif keep.start.z < remove.start.z < keep.end.z:
        z = remove.start.z
        a = __copy_for_z(keep, z, True)
        keep.end.z = z - 1
        if not a.inside(remove):
            blocks.append(a)
            __diff(a, remove, blocks)
