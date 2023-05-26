"""4:40pm 4:48pm

idk why this is greedy..."""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_sum = 0
        last_best = float("-inf")
        for n in nums:
            now_best = max(n, n + last_best)
            max_sum = max(now_best, max_sum)
            last_best = now_best

        return max_sum
