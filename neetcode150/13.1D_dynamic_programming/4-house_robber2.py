"""1:56pm - 2:13pm"""
from typing import List


def get_reg_sol(nums):
    a1, a2 = nums[0], max(nums[:2])

    curr = 2
    while curr < len(nums):
        num = nums[curr]
        a3 = max(a1 + num, a2)
        a1, a2 = a2, a3
        curr += 1

    return max(a1, a2)


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
