"""4:50pm 
4:57pm time out
4:59pm time out pt 2
5:02pm time out pt 3
5:07pm got optimal solution
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_reachable = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if last_reachable - i <= nums[i]:
                last_reachable = i
        return last_reachable == 0
