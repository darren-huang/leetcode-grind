"""1:13pm - 1:25pm"""
from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build adj map
        graph = defaultdict(list)  # maps node -> List[(neighbor_node, edge_weight)]
        for u, v, w in times:
            graph[u].append((v, w))

        # dumb dijkstras
        visited = set()
        min_heap = [(0, k)]  # minheap with (priority, node)
        max_time = 0
        while min_heap:
            time_for_sig_to_reach, next_to_visit = heapq.heappop(min_heap)
            if next_to_visit not in visited:
                max_time = max(max_time, time_for_sig_to_reach)
                visited.add(next_to_visit)

                for neighbor, edge_weight in graph[next_to_visit]:
                    if neighbor not in visited:
                        heapq.heappush(
                            min_heap, (time_for_sig_to_reach + edge_weight, neighbor)
                        )

        if n == len(visited):
            return max_time
        else:
            return -1
