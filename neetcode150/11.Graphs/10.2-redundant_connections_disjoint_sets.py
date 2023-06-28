from typing import List
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [0] + list(range(1, len(edges) + 1))
        weight = [0] + ([1] * len(edges))

        def get_root(v: int) -> int:
            if parent[v] == v:
                return v
            else:
                root = get_root(parent[v])
                parent[v] = root  # path compression
                return root

        def join(v: int, u: int) -> None:
            rv, ru = get_root(v), get_root(u)
            if weight[rv] < weight[ru]:
                parent[rv] = ru
                weight[ru] += weight[rv]
            else:
                parent[ru] = rv
                weight[rv] += weight[ru]

        for e1, e2 in edges:
            if get_root(e1) == get_root(e2):
                # already connected:
                return [e1, e2]
            else:
                join(e1, e2)
        return []
