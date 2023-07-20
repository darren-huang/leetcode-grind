"""8:14pm - giveup


no good way of doing dfs without recursion
possible but messy

10pm switching to toplogical sort, kahn's algorithm
10:09pm done
"""

from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # get adj_matrix
        adj_matrix = defaultdict(list)
        for pre_req, course in prerequisites:
            adj_matrix[pre_req].append(course)

        # get indegree counts
        zero_degree_set = set(range(numCourses))
        in_degree_count = defaultdict(lambda: 0)
        for in_degree_nodes in adj_matrix.values():
            for in_degree_node in in_degree_nodes:
                in_degree_count[in_degree_node] += 1
                if in_degree_node in zero_degree_set:
                    zero_degree_set.remove(in_degree_node)

        zero_degree_list = list(zero_degree_set)
        topological_sorted = []
        while zero_degree_list:
            node = zero_degree_list.pop()
            topological_sorted.append(node)
            for child in adj_matrix[node]:
                in_degree_count[child] -= 1
                if in_degree_count[child] == 0:
                    zero_degree_list.append(child)

        return len(topological_sorted) == numCourses
