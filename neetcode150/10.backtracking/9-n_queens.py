"""8:30pm
8:50pm"""
from typing import List


def help_check_queens_diag_ok(row_i_to_col_i, curr_row_i, curr_col_i):
    for row_i, col_i in row_i_to_col_i.items():
        if abs(col_i - curr_col_i) == abs(row_i - curr_row_i):
            return False
    return True


def dict_to_board(row_i_to_col_i: dict, n: int):
    ret_board = []
    for row_i in range(n):
        col_i = row_i_to_col_i[row_i]
        ret_board.append(("." * col_i) + "Q" + ("." * (n - col_i - 1)))
    return ret_board


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret_combos = []

        # each entry shows which col for the queen on the i'th row
        row_i_to_col_i = {}
        free_rows = set(range(n))

        def dfs(col):
            # base case
            if col >= n:
                ret_combos.append(dict_to_board(row_i_to_col_i, n))
                return

            for row_i in list(free_rows):
                if help_check_queens_diag_ok(row_i_to_col_i, row_i, col):
                    # place the queen
                    row_i_to_col_i[row_i] = col
                    free_rows.remove(row_i)

                    # dfs traverse to next queen
                    dfs(col + 1)

                    # unplace the queen
                    del row_i_to_col_i[row_i]
                    free_rows.add(row_i)

        dfs(0)
        return ret_combos
