"""12:45pm - 1:05pm

think about all cases before proceeding"""

from typing import List


# [a  |    x        b]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low_i, high_i = 0, len(nums) - 1

        while low_i <= high_i:
            mid_i = (low_i + high_i) // 2
            if nums[mid_i] == target:
                return mid_i
            if nums[0] <= nums[mid_i]:
                # boundary to the right
                if nums[0] <= target and target < nums[mid_i]:
                    # move search window left
                    high_i = mid_i - 1
                else:
                    low_i = mid_i + 1
            else:
                # boundary to the left
                if nums[mid_i] < target and target <= nums[-1]:
                    # move search window right
                    low_i = mid_i + 1
                else:
                    high_i = mid_i - 1

        return -1
