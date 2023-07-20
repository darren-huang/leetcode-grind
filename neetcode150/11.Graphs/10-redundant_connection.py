from typing import List
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # build graph
        adj_matrix = defaultdict(set)
        for e1, e2 in edges:
            adj_matrix[e1].add(e2)
            adj_matrix[e2].add(e1)

        # find cycle inside this graph (must exist)
        path_so_far = [1]
        so_far_set = set([1])
        path_found = False

        def dfs(v):
            print(v)
            nonlocal path_found
            # visit v
            for u in adj_matrix[v]:
                if u not in so_far_set:
                    # rm edge & update path
                    path_so_far.append(u)
                    so_far_set.add(u)
                    adj_matrix[u].remove(v)
                    adj_matrix[v].remove(u)

                    # recurse
                    dfs(u)
                    if path_found:
                        return

                    # add back edge and rm path
                    path_so_far.pop()
                    so_far_set.remove(u)
                    adj_matrix[u].add(v)
                    adj_matrix[v].add(u)
                else:
                    # cycle found
                    path_so_far.append(u)
                    path_found = True
                    return

        dfs(1)
        if not path_found:
            raise ValueError("No cycle found")

        edge_to_index = {tuple(sorted(e)): i for i, e in enumerate(edges)}
        cycle_end = prev = path_so_far[-1]
        ret = []
        ret_i = -1
        for v in path_so_far[-2::-1]:
            edge = tuple(sorted([prev, v]))
            if ret_i < edge_to_index[edge]:
                ret, ret_i = edge, edge_to_index[edge]
            if cycle_end == v:
                break
            prev = v

        return list(ret)
