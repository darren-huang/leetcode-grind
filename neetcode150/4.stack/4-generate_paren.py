"""10:56am - 11:01am

backtrack remember to return!!! upon adding"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combo = []
        curr_parens = []

        def dfs(n_open_left, n_close_possible):
            if n_open_left == 0 and n_close_possible == 0:
                combo.append("".join(curr_parens))
                # RETRUN HERE (doesn't matter for this problem but would be a bug in the future)

            if n_open_left > 0:
                curr_parens.append("(")
                dfs(n_open_left - 1, n_close_possible + 1)
                curr_parens.pop()

            if n_close_possible > 0:
                curr_parens.append(")")
                dfs(n_open_left, n_close_possible - 1)
                curr_parens.pop()

        dfs(n, 0)
        return combo
