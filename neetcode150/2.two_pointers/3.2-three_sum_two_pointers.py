"""3:44pm - 3:48pm


ensure that all cases get updated.
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        for i in range(len(nums) - 1):
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == 0:
                    triplets.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1
        return list(triplets)
