"""1:06pm - 1:14pm"""

from typing import List
from collections import defaultdict


def is_in(given_set, item):
    if item in given_set:
        return True
    else:
        given_set.add(item)
        return False


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_to_number_set = defaultdict(set)
        col_to_number_set = defaultdict(set)

        for box_i in range(3):
            for box_j in range(3):
                box_number_set = set()
                for i in range(box_i * 3, (box_i * 3) + 3):
                    for j in range(box_j * 3, (box_j * 3) + 3):
                        item = board[i][j]
                        if item != ".":
                            if (
                                is_in(row_to_number_set[i], item)
                                or is_in(col_to_number_set[j], item)
                                or is_in(box_number_set, item)
                            ):
                                return False
        return True
