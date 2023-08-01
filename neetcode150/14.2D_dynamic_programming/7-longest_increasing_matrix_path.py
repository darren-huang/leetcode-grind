"""4:27pm - 4:37pm"""

from typing import List


def get_children(i, j, n, m):
    return [
        (c_i, c_j)
        for c_i, c_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        if c_i >= 0 and c_j >= 0 and c_i < n and c_j < m
    ]


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        longest_path_len = 0
        n, m = len(matrix), len(matrix[0])
        seen = {}

        def dfs(i, j):
            if (i, j) in seen:
                return seen[(i, j)]

            ret = 1
            for c_i, c_j in get_children(i, j, n, m):
                if matrix[i][j] < matrix[c_i][c_j]:
                    # can i,j -> c_i,c_j
                    ret = max(ret, dfs(c_i, c_j) + 1)

            seen[(i, j)] = ret
            return ret

        for i in range(n):
            for j in range(m):
                longest_path_len = max(dfs(i, j), longest_path_len)

        return longest_path_len
