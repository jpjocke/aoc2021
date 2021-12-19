from typing import List

from point3D import Point3D
from src.day19.scanner import Scanner


def parse_scanners(data: List[str]) -> List[Scanner]:
    scanners = []

    for line in data:
        if len(line) == 0:
            continue
        if line.startswith('---'):
            scanner = Scanner(len(scanners))
            scanners.append(scanner)
            continue
        x, y, z = line.split(',')
        beacon = Point3D(int(x), int(y), int(z))
        scanner.add_beacon(beacon)
    scanners[0].pos = Point3D(0, 0, 0)
    return scanners
