"""10:31am"""
from typing import List


#  3 3
# [1 2 3]
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0: -1}
        curr_sum = 0
        for i, n in enumerate(nums):
            curr_sum = (curr_sum + n) % k

            if curr_sum not in seen:
                seen[curr_sum] = i
            elif i - seen[curr_sum] >= 2:
                return True
        return False
