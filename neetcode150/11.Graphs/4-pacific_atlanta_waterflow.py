"""4:01pm
4:33pm


FOR THE LOVE OF GOD
DO
NOT
USE
[[]*x]*x
ITS A MISTAKE

use [[False] * x for _ in range(x)]
"""

from typing import List


def get_child(i, j, heights):
    """Uses reverse logic for finding flow, ie. can child flow TO i, j"""
    n, m = len(heights), len(heights[0])
    children = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    curr_height = heights[i][j]
    return [
        c
        for c in children
        if c[0] >= 0
        and c[0] < n
        and c[1] >= 0
        and c[1] < m
        and curr_height <= heights[c[0]][c[1]]
    ]


def reverse_dfs(heights, initial_stack):
    n, m = len(heights), len(heights[0])
    reachable = [[False] * m for i in range(n)]
    seen = set(initial_stack)
    while initial_stack:
        i, j = initial_stack.pop()
        reachable[i][j] = True
        for c_i, c_j in get_child(i, j, heights):
            if (c_i, c_j) not in seen:
                seen.add((c_i, c_j))
                initial_stack.append((c_i, c_j))
    return reachable


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        p_stack = [(0, x) for x in range(0, m)] + [(x, 0) for x in range(1, n)]
        pacific_reachable = reverse_dfs(heights, p_stack)
        a_stack = [(n - 1, x) for x in range(0, m)] + [
            (x, m - 1) for x in range(0, n - 1)
        ]
        atlantic_reachable = reverse_dfs(heights, a_stack)

        ret_coords = []
        for i in range(n):
            for j in range(m):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    ret_coords.append([i, j])
        return ret_coords
