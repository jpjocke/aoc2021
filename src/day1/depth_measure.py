from typing import List


class DepthMeasure:

    def count(self, data: List[int]) -> int:
        count = 0
        for i, val in enumerate(data):
            if i == 0:
                continue
            if val > data[i - 1]:
                count += 1
        return count

    def spread_list(self, data: List[int], spread_size: int) -> List[int]:
        spread = []
        for i, val in enumerate(data):
            if (i + spread_size) > len(data):
                break
            count = 0
            for y in range(0, spread_size):
                count += data[i + y]
            spread.append(count)
        return spread
