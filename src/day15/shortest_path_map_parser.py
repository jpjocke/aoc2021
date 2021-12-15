from typing import List

from src.day15.node import Node
from util import get_key


def __link_key(shortest_map: {str, Node}, node: Node, i: int, j: int):
    key = get_key(i, j)
    if key in shortest_map:
        inner_node = shortest_map[key]
        node.paths.append(inner_node)


def __link(shortest_map: {str, Node}, i: int, j: int):
    key = get_key(i, j)
    node = shortest_map[key]
    __link_key(shortest_map, node, i - 1, j)
    __link_key(shortest_map, node, i + 1, j)
    __link_key(shortest_map, node, i, j - 1)
    __link_key(shortest_map, node, i, j + 1)


def parse_shortest_input(data: List[str]) -> {str, Node}:
    shortest_map = {}
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            key = get_key(i, j)
            node = Node(key, int(val))
            shortest_map[key] = node

    for i, row in enumerate(data):
        for j, val in enumerate(row):
            __link(shortest_map, i, j)

    # no cost for the first
    shortest_map[get_key(0, 0)].cost = 0
    shortest_map[get_key(0, 0)].path_cost = 0
    return shortest_map
