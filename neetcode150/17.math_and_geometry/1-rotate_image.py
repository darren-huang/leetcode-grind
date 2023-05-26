"""10:25am - 10:38am"""

from typing import List


def rotate_index(i, j, n):
    """rotate index 90 degrees clockwise"""
    return (j, (n - 1 - i))


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for i in range((n + 1) // 2):
            for j in range(n // 2):
                i1 = (i, j)
                i2 = rotate_index(*i1, n)
                i3 = rotate_index(*i2, n)
                i4 = rotate_index(*i3, n)
                (
                    matrix[i1[0]][i1[1]],
                    matrix[i2[0]][i2[1]],
                    matrix[i3[0]][i3[1]],
                    matrix[i4[0]][i4[1]],
                ) = (
                    matrix[i4[0]][i4[1]],
                    matrix[i1[0]][i1[1]],
                    matrix[i2[0]][i2[1]],
                    matrix[i3[0]][i3[1]],
                )
