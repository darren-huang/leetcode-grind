"""start 11:03am

finish11:09am

check index with small example"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        total_indices = num_rows * num_cols
        lower_i, upper_i = 0, total_indices - 1

        while lower_i <= upper_i:
            # convert to row and column:
            index = (lower_i + upper_i) // 2
            row = index // num_cols
            col = index % num_cols
            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                lower_i = index + 1
            else:
                upper_i = index - 1

        return False
