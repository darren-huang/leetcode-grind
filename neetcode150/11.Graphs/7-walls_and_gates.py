"""10:43pm - 10:58pm"""

from typing import (
    List,
)


def get_children(i, j, n, m):
    return [
        (c_i, c_j)
        for c_i, c_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        if c_i >= 0 and c_j >= 0 and c_i < n and c_j < m
    ]


WALL = -1
GATE = 0
EMPTY = 2147483647


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        n, m = len(rooms), len(rooms[0])
        next_distance = 0
        next_indicies = set()  # represents all rooms with the current distance
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == GATE:
                    next_indicies.add((i, j))

        while next_indicies:
            curr_indices, next_indicies = next_indicies, set()
            next_distance += 1
            for i, j in curr_indices:
                for c_i, c_j in get_children(i, j, n, m):
                    c_room = rooms[c_i][c_j]
                    if c_room == EMPTY:
                        rooms[c_i][c_j] = next_distance
                        next_indicies.add((c_i, c_j))

        return rooms
