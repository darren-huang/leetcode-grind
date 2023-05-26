"""10:06am - 10:23am

greedy problem....
i'm bad at these lmao
"""

from typing import List


def overlap(s1, e1, s2, e2):
    return not (e1 <= s2 or e2 <= s1)


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals.sort()

        min_to_remove = float("inf")

        def dfs(last_i, i, n_remove):
            nonlocal min_to_remove
            # print(last_i, i, n_remove)

            # base case
            if i >= len(intervals):
                min_to_remove = min(min_to_remove, n_remove)
                return

            # recurrant relation
            if overlap(*intervals[last_i], *intervals[i]):
                if intervals[last_i][1] < intervals[i][1]:
                    dfs(last_i, i + 1, n_remove + 1)
                else:
                    dfs(i, i + 1, n_remove + 1)
            else:
                dfs(i, i + 1, n_remove)

        # print(intervals)
        dfs(0, 1, 0)
        return min_to_remove
