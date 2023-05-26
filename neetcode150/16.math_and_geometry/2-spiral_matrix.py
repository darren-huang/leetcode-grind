"""10:40 - 10:50am"""

from typing import List


def update_direction(i, j):
    return j, -i


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        seen = set()
        direction = (0, 1)
        c_i, c_j = 0, 0
        n, m = len(matrix), len(matrix[0])

        def is_valid(i, j):
            return (i, j) not in seen and i >= 0 and j >= 0 and i < n and j < m

        while len(seen) < n * m:
            ret.append(matrix[c_i][c_j])
            seen.add((c_i, c_j))

            # get new index
            if not is_valid(c_i + direction[0], c_j + direction[1]):
                direction = update_direction(direction)
            c_i, c_j = c_i + direction[0], c_j + direction[1]
        return ret
        
