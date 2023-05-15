"""11:09am - 11:38am"""

from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(defaultdict(lambda: 0))
        for from_aiport, to_airport in tickets:
            graph[from_aiport][to_airport] += 1
        for edges in graph.values():
            edges.sort()

        def remove_edge(from_air, to_air):
            graph[from_air][to_air] -= 1
            if graph[from_air][to_air] == 0:
                del graph[from_air][to_air]

        # dfs
        curr_path = []
        num_edges = len(tickets)

        def dfs(airport):
            # if no edges left in graph
            if num_edges == 0:
                return True  # path found

            for to_airport in graph[airport]:
                remove_edge(airport, to_airport)
                curr_path.append(to_airport)
                num_edges -= 1

                if dfs(to_airport):
                    return True

                num_edges += 1
                graph[from_aiport][to_airport] += 1
                curr_path.pop()

        return curr_path
