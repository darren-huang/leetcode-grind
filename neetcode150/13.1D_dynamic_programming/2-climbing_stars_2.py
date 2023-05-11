"""9:02pm 9:11pm"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        last_min_2, last_min_1 = 0, 0
        cost = [0, 0] + cost
        for i in range(len(cost) - 1):
            last_min_2, last_min_1 = last_min_1, min(
                cost[i] + last_min_2, cost[i + 1] + last_min_1
            )
        return last_min_1
