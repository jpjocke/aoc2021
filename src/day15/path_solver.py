from src.day15.node import Node
from util import get_key


def solve(s_map: {str, Node}) -> {str, Node}:
    to_solve = [get_key(0, 0)]
    while True:
        if len(to_solve) == 0:
            break
        node = s_map[to_solve[0]]
        to_solve.remove(to_solve[0])
        if node.checked:
            continue
        node.checked = True
        for inner_node in node.paths:
            to_solve.append(inner_node.identifier)
            if (inner_node.cost + node.path_cost) < inner_node.path_cost:
                inner_node.path_cost = inner_node.cost + node.path_cost
                inner_node.from_path = node
    return s_map
