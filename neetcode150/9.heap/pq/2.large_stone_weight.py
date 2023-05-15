"""4:22pm
4:32pm

note: do not try to use maxheap functions
just make the numbers negative
"""
from typing import List

import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n_stones = [-s for s in stones]
        heapq.heapify(n_stones)
        while len(n_stones) > 1:
            s1, s2 = heapq.heappop(n_stones), heapq.heappop(n_stones)
            if s1 == s2:
                continue
            else:
                heapq.heappush(n_stones, -abs(s1 - s2))
        return -n_stones[0] if n_stones else 0

