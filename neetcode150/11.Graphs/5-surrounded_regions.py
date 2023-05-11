"""5:19pm
5:33pm"""
from typing import List


def get_child(i, j, n, m):
    children = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    return [
        (ci, cj) for ci, cj in children if ci >= 0 and ci < n and cj >= 0 and cj < m
    ]


def is_edge(i, j, n, m):
    return i == 0 or j == 0 or i == n - 1 or j == m - 1


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n, m = len(board), len(board[0])
        visited = set()
        for i in range(n):
            for j in range(m):
                index, item = (i, j), board[i][j]
                if index not in visited and item == "O":
                    # setup dfs
                    visited.add(index)
                    stack = [index]
                    curr_Os = []
                    captured = True

                    # dfs on index
                    while stack:
                        next_index = stack.pop()
                        curr_Os.append(next_index)
                        if is_edge(next_index[0], next_index[1], n, m):
                            captured = False

                        for c in get_child(next_index[0], next_index[1], n, m):
                            if c not in visited:
                                visited.add(c)
                                if board[c[0]][c[1]] == "O":
                                    stack.append(c)

                    if captured:
                        for cap_index in curr_Os:
                            board[cap_index[0]][cap_index[1]] = "X"
        return board
