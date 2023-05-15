"""3:15pm
3:28pm"""

from typing import List


def helper_get_children(i, j, grid):
    n, m = len(grid), len(grid[0])
    children = [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]
    return [c for c in children if c[0] >= 0 and c[0] < n and c[1] >= 0 and c[1] < m]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0" or (i, j) in seen:
                    continue
                else:
                    # run dfs on land to get all connected land
                    stack = [(i, j)]  # BUG didn't add (i,j) to the seen set
                    while stack:
                        ni, nj = stack.pop()
                        for c in helper_get_children(ni, nj, grid):
                            if c not in seen:
                                seen.add(c)
                                if grid[c[0]][c[1]] == "1":
                                    stack.append(c)

                    num_islands += 1
        return num_islands
