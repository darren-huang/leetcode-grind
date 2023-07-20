"""9:40am 
coding done 9:55am

1 bug
9:58am


2 bfs's probably will need 2 sets"""
from typing import List
import heapq


def get_children(i, j, n, m):
    candidates = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    return [
        (ci, cj) for ci, cj in candidates if ci >= 0 and cj >= 0 and ci < n and cj < m
    ]


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        mheap = [(grid[0][0], (0, 0))]  # stores (elevation, index)
        seen = set([(0, 0)])
        visited = set()
        t = 0
        n, m = len(grid), len(grid[0])

        while (n - 1, m - 1) not in visited:
            # pop next item
            elev, (i, j) = heapq.heappop(mheap)

            # update elevation
            t = max(t, elev)

            # run bfs for working elevations, non-working elevations get added to mheap
            stack = [(i, j)]
            while stack:
                i2, j2 = stack.pop()
                visited.add((i2, j2))
                for ci, cj in get_children(i2, j2, n, m):
                    if (ci, cj) not in seen:
                        if grid[ci][cj] <= t:
                            # can swim here with 0 time
                            stack.append((ci, cj))
                        else:
                            # will need to update t to swim here
                            heapq.heappush(mheap, (grid[ci][cj], (ci, cj)))
                        seen.add((ci, cj))

        return t
