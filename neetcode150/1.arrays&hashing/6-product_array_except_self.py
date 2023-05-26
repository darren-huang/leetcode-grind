"""1:00pm - 1:05pm"""
from typing import List
from collections import deque


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prods = [1]
        right_prods = deque([1])
        for i in range(1, len(nums)):
            left_prods.append(left_prods[i - 1] * nums[i - 1])
        for i in range(len(nums) - 2, -1, -1):
            right_prods.appendleft(right_prods[0] * nums[i + 1])

        ans = []
        for i in range(len(nums)):
            ans.append(left_prods[i] * right_prods[i])

        return ans
