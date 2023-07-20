"""10:49am - 11:14am"""
from typing import List, Tuple, Dict
from collections import defaultdict

# dumb dijkstras
import heapq


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # make adj_matrix
        adj_matrix: Dict[int, Dict[int, int]] = defaultdict(dict)
        for from_, to_, price in flights:
            adj_matrix[from_][to_] = price

        dumb_pq: List[Tuple[int, int, int]] = [(0, -1, src)]  # (cost, stops, node)
        seen: Dict[Tuple[int, int], int] = {
            (src, -1): 0
        }  # seen dict mapping from node -> num_k
        # item is NOT seen if k < seen[src]

        while dumb_pq:
            cost, curr_k, node = heapq.heappop(dumb_pq)
            # print(cost, curr_k, node)
            if node == dst:
                return cost
            # print(adj_matrix[node])
            for child, price in adj_matrix[node].items():
                # print(" ", seen, child, price)
                if curr_k + 1 == k and child != dst:
                    continue
                # print("continue")
                key = (child, curr_k + 1)
                ncost = cost + price
                if key not in seen or seen[key] > ncost:
                    heapq.heappush(dumb_pq, (ncost, curr_k + 1, child))
                    seen[key] = ncost

        return -1
