"""5:09pm - 5:23pm

took some work"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        mins = [float("inf")] * len(nums)
        mins[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            # iterate backwards
            j = min(nums[i] + i, len(nums) - 1)
            mins[i] = mins[j] + 1
            while mins[i + 1] > mins[i]:
                mins[i + 1] = mins[i]
                i += 1
        return mins[0]
