"""
Really fast, no bugs!

good work @ me

idea was pretty simple, ie. reuse the current space

what tripped me up was thinking about worst case runtime

turns out still is O(n)
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            done = False

            while not done:
                val = nums[index]
                if 1 <= val and val <= len(nums):
                    if nums[val - 1] != val:
                        next_num = nums[val - 1]
                        nums[val - 1] = val
                        nums[index] = next_num
                        continue
                done = True
        for index in range(len(nums)):
            if nums[index] != index + 1:
                return index + 1
        return len(nums) + 1
