"""2:51pm - 3:14pm timeout
3:24pm


think about... can i identify the end of a sequence
and then can i just iterate over it one time.
"""
from typing import List
from collections import deque


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        num_to_sequences = {}  # num -> (min, max)
        for n in nums:
            if n in seen:
                continue
            seen.add(n)

            smin, smax = n, n
            if n - 1 in num_to_sequences:
                smin = num_to_sequences[n - 1][0]
            if n + 1 in num_to_sequences:
                smax = num_to_sequences[n + 1][1]
            num_to_sequences[smin] = (smin, smax)
            num_to_sequences[smax] = (smin, smax)

        max_len = 0
        for seq in num_to_sequences.values():
            max_len = max(max_len, seq[1] - seq[0] + 1)

        return max_len
