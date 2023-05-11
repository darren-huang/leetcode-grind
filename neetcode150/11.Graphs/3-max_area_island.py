"""
3:42pm
finish coding 3:52 but error
3:56pm

Don't forget correct initialization of the seen set
"""
from typing import List


def get_children(i, j, n, m):
    children = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    return [c for c in children if c[0] >= 0 and c[0] < n and c[1] >= 0 and c[1] < m]


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island_area = 0
        visited = set()
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                item = grid[i][j]
                if (i, j) not in visited and item == 1:
                    # run dfs on i,j
                    stack = [(i, j)]
                    visited.add((i, j))
                    area = 0

                    while stack:
                        n_i, n_j = stack.pop()
                        area += 1
                        for c_i, c_j in get_children(n_i, n_j, n, m):
                            if (c_i, c_j) not in visited:
                                visited.add((c_i, c_j))
                                if grid[c_i][c_j] == 1:  # is land
                                    stack.append((c_i, c_j))
                    print(area)
                    max_island_area = max(max_island_area, area)

        return max_island_area
