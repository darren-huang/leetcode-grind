"""9:59pm - 10:14pm"""
from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg_cnt = defaultdict(lambda: 0)
        adj_matrix = defaultdict(list)
        # count in_degree of courses
        for v2, v1 in prerequisites:
            indeg_cnt[v2] += 1
            adj_matrix[v1].append(v2)

        # get set of in_degree == 0
        zero_degree_stack = [v for v in range(numCourses) if indeg_cnt[v] == 0]
        answer = []

        # process each vertex with 0 degree:
        while zero_degree_stack:
            next_zero_vertex = zero_degree_stack.pop()
            answer.append(next_zero_vertex)
            for to_v in adj_matrix[next_zero_vertex]:
                indeg_cnt[to_v] -= 1
                if indeg_cnt[to_v] == 0:
                    zero_degree_stack.append(to_v)

        # check that we have enough courses included
        if len(answer) == numCourses:
            return answer
        return []
