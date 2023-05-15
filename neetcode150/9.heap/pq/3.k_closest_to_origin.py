"""4:33pm - 4:40pm"""

from typing import Optional, List
import heapq


class Point:
    def __init__(self, point) -> None:
        self.x, self.y = point[0], point[1]
        self.point = point

    def get_dist(self):
        return ((self.x**2) + (self.y**2)) ** 0.5

    def __eq__(self, __value: object) -> bool:
        return self.get_dist() == __value.get_dist()

    def __lt__(self, __value: object) -> bool:
        return self.get_dist() < __value.get_dist()


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_objs = [Point(p) for p in points]
        heapq.heapify(point_objs)
        return [heapq.heappop(point_objs).point for _ in range(k)]
