from typing import List

from src.day12.cavern import Cavern


def clean_edges(key_map: {str, Cavern}) -> {str, Cavern}:
    key_map2 = {}
    for key in key_map:
        if not key_map[key].only_small_connections():
            key_map2[key] = key_map[key]
        else:
            key_map[key].remove_connection()
    return key_map2


def dfs(key_map: {str, Cavern}) -> int:
    paths = []
    __dfs_inner(key_map['start'], '', paths)
    return len(paths)


def __dfs_inner(start: Cavern, path: str, paths: List[str]):
    path += '-' + start.identifier
    if start.is_end:
        paths.append(path)
        return
    for c in start.connections:
        if c.is_start:
            continue
        if c.is_small and c.identifier in path.split('-'):
            continue
        __dfs_inner(c, path, paths)
