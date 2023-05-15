"""12:47pm - 1:06pm

important lesson

priority Queue is needed in order to get best runtime
E log(V), in this case E = N*N or V*V  since it is a strongly connected graph

alternative is to just use a dumbe PQ ie. 
instead of doing an update priority, you just repush the item
Also instead of creating a whole new class object to represent the item, use a tuple
ie. (priority, item)


new runtime is E log(E) since in the worst case there is a better edge weight each time, and the PQ will hold E items (one priority for every edge)
"""
from typing import List
import heapq


def get_cost(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_heap = [(0, points[0])]  # min_dist, and point
        un_connected = {tuple(pt) for pt in points}
        total_cost = 0
        while un_connected:
            cost, next_pt = heapq.heappop(min_heap)

            if tuple(next_pt) in un_connected:
                # connect that edge / pt
                un_connected.remove(tuple(next_pt))
                total_cost += cost

                # update costs
                for pt in un_connected:
                    heapq.heappush(min_heap, (get_cost(pt, next_pt), pt))

        return total_cost
