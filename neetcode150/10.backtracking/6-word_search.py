"""7:51pm

kinda dumb, all solutions i've seen just try to add a short cut optimization that avoids last problem
"""
from typing import List
from collections import defaultdict


def get_children(i, j, n, m):
    candidates = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    return [
        (c_i, c_j)
        for c_i, c_j in candidates
        if c_i >= 0 and c_j >= 0 and c_i < n and c_j < m
    ]


def search(board, word, i, j, n, m):
    curr_word = board[i][j]
    if curr_word != word[0]:
        return False
    is_found = False
    seen = set([(i, j)])

    def dfs(i, j):
        """process word for backtracking"""
        nonlocal curr_word, is_found
        if is_found or len(curr_word) == len(word):
            is_found = True
            return

        for c_i, c_j in get_children(i, j, n, m):
            c_char = board[c_i][c_j]
            if c_char == word[len(curr_word)] and (c_i, c_j) not in seen:
                # setup candidate
                curr_word += c_char
                seen.add((c_i, c_j))

                dfs(c_i, c_j)

                # remove candidate
                curr_word = curr_word[:-1]
                seen.remove((c_i, c_j))

    dfs(i, j)
    return is_found


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wlet_count = defaultdict(lambda: 0)
        for c in word:
            wlet_count[c] += 1

        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                c = board[i][j]
                if c in wlet_count:
                    wlet_count[c] -= 1
        if any([count > 0 for count in wlet_count.values()]):
            return False
        

        for i in range(n):
            for j in range(m):
                if search(board, word, i, j, n, m):
                    return True
        return False
