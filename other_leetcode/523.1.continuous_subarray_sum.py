"""9:42am"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for window_len in range(2, len(nums) + 1):
            curr_sum = 0
            left = 0
            for i, n in enumerate(nums):
                # add new number
                curr_sum = (curr_sum + n) % k

                # check if we need to remove old number
                if i - left + 1 > window_len:
                    curr_sum = (curr_sum - nums[left]) % k
                    left += 1

                # check if zero
                if i - left + 1 == window_len:
                    if curr_sum == 0:
                        return True
        return False
