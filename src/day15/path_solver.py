from typing import Set

from src.day15.node import Node
from util import get_key


def solve_full_djikstra(s_map: {str, Node}) -> {str, Node}:
    to_solve: Set[Node] = {s_map[get_key(0, 0)]}
    while True:
        node = find_lowest_unvisited(to_solve)
        if node is None:
            break
        node.checked = True
        to_solve.remove(node)
        for inner_node in node.paths:
            if not inner_node.checked:
                to_solve.add(inner_node)
            value = inner_node.cost + node.path_cost
            if value < inner_node.path_cost:
                inner_node.path_cost = value
                inner_node.from_path = node

    return s_map


def find_lowest_unvisited(to_solve: Set[Node]) -> Node:
    l_val = 9999999999999
    l_node = None
    for node in to_solve:
        if node.checked:
            continue
        if node.path_cost < l_val:
            l_val = node.path_cost
            l_node = node
    return l_node


def print_values(s_map: {str, Node}, max_i: int, max_j: int):
    sb = ''
    for i in range(max_i + 1):
        for j in range(max_j + 1):
            key = get_key(i, j)
            sb += str(s_map[key].cost)
        sb += '\n'
    print(sb)


def print_path(s_map: {str, Node}, max_i: int, max_j: int):
    sb = ''
    for i in range(max_i + 1):
        for j in range(max_j + 1):
            key = get_key(i, j)
            sb += str(s_map[key].show_path())
        sb += '\n'
    print(sb)
