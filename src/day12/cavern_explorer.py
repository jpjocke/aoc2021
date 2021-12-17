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


def dfs(key_map: {str, Cavern}, twice: bool) -> int:
    paths = []
    __dfs_inner(key_map['start'], '', paths, twice)
    return len(paths)


def __dfs_inner(start: Cavern, path: str, paths: List[str], twice: bool):
    path += '-' + start.identifier
    if start.is_end:
        paths.append(path)
        return
    for c in start.connections:
        if c.is_start:
            continue
        if c.is_small and __visited(c, path, twice):
            continue
        __dfs_inner(c, path, paths, twice)


def __visited(c: Cavern, path: str, twice: bool) -> bool:
    if not twice:
        return c.identifier in path.split('-')
    for visited in path.split('-'):
        if len(visited) == 0 or visited == 'start':
            continue
        if visited[0].isupper():
            continue
        count = 0
        for v2 in path.split('-'):
            if visited == v2:
                count += 1
                if count == 2:
                    return c.identifier in path.split('-')
    return False
