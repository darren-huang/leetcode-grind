"""10:18am
10:32am

just a calculation bug 


"""

from typing import List


def help_get_children(i, j, n, m):
    return [
        index
        for index in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        if index[0] >= 0 and index[1] >= 0 and index[0] < n and index[1] < m
    ]


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        curr_rottens, next_rottens = [], []
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    next_rottens.append((i, j))

        # update rotten oranges until completion
        num_minutes = 0
        while next_rottens:
            curr_rottens, next_rottens = next_rottens, []
            for i, j in curr_rottens:
                for c_i, c_j in help_get_children(i, j, n, m):
                    if grid[c_i][c_j] == 1:  # fresh orange
                        # convert orange
                        grid[c_i][c_j] = 2

                        # enque the orange for the next round
                        next_rottens.append((c_i, c_j))
            if next_rottens:
                num_minutes += 1

        # check if any are not rotten anymore
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return num_minutes
