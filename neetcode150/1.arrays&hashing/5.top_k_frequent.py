"""10:57pm - 11:03pm

current is nlogn
O(n) possible, sort using Bucket Sort (since frequencies must sum up to N)
O(n log K ) possible with a heap
"""

from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(lambda: 0)
        for n in nums:
            freq[n] += 1
        top_k = sorted(freq.items(), key=lambda t: t[1])
        return [t[0] for t in top_k[-k:]]
