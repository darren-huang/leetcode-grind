"""Same solution as previous question

took 6 minutes
small misunderstanding of question.
"""

from typing import (
    List,
)


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        parents = list(range(n))
        weights = [1] * n
        num_components = n

        def _get_root(i):
            # no path compression
            while parents[i] != i:
                i = parents[i]
            return i

        for e1, e2 in edges:
            # check if connected
            r1, r2 = _get_root(e1), _get_root(e2)
            if r1 == r2:
                return False
            else:
                # connect r1, and r2
                if weights[r1] < weights[r2]:
                    r1, r2 = r2, r1
                # r1 is now bigger
                parents[r2] = r1  # small points to big
                weights[r1] += weights[r2]
                num_components -= 1
        return num_components == 1
