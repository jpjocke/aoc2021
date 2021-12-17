from typing import List

from point import Point


class Area:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def find_highest(self, start_y, max_y) -> (int, int):
        largest = 0
        highest = 0
        for y in range(start_y, max_y):
            hits, h = self.__sim_y(y)
            if len(hits) > 0:
                largest = y
                highest = h
        return largest, highest

    def find_trajectory_count(self, x_s: int, x_e: int, y_s: int, y_e: int) -> int:
        # find starting trajectory for x and y separately. also count all steps that trajectory is within the goal
        # combine all trajectories with the same amount of steps.
        ys = self.find_y(y_s, y_e)
        xs = self.find_x(x_s, x_e)
        trajectories = set([])
        for x, step_x in xs:
            for y, step_y in ys:
                if step_x == step_y:
                    trajectories.add(Point(x, y))
        return len(trajectories)

    def find_y(self, start_y, max_y) -> List[object]:
        all_hits = []
        for y in range(start_y, max_y):
            hits, h = self.__sim_y(y)
            if len(hits) > 0:
                for step in hits:
                    all_hits.append((y, step))
        return all_hits

    def find_x(self, start_x, max_x) -> List[object]:
        all_hits = []
        for x in range(start_x, max_x):
            hits = self.__sim_x(x)
            if len(hits) > 0:
                for step in hits:
                    all_hits.append((x, step))
        return all_hits

    def __sim_y(self, velocity_y: int) -> (List[int], int):
        y = 0
        highest = 0
        steps = 0
        hits = []
        while True:
            y += velocity_y
            steps += 1
            if y > highest:
                highest = y
            if y < self.end.y:
                break
            if y <= self.start.y:
                hits.append(steps)
            velocity_y -= 1
        return hits, highest

    def __sim_x(self, velocity_x: int) -> List[int]:
        x = 0
        steps = 0
        hits = []
        while True:
            x += velocity_x
            steps += 1
            if x > self.end.x:
                break
            if x >= self.start.x:
                hits.append(steps)
            if velocity_x > 0:
                velocity_x -= 1
            if velocity_x < 0:
                velocity_x += 1

            if steps > 250:  # magic number tested with my input
                break
        return hits
