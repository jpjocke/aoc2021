from typing import List

from src.day13.fold import Fold
from point import Point
from src.day13.folder import Folder


def parse_folds(data: List[str]) -> Folder:
    folder = Folder()
    folds = False
    for line in data:
        if line == '':
            folds = True
        elif folds:
            s = line.split(' ')
            k = s[2].split('=')
            folder.add_fold(Fold(k[0], int(k[1])))
        else:
            p = line.split(',')
            folder.add_pos(Point(int(p[0]), int(p[1])))
    return folder
