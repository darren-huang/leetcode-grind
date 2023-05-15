"""4:11pm - 4:16pm"""

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        seen = {}

        def recurse(nums, target):
            # base case
            if not nums:
                return 1 if target == 0 else 0

            key = (tuple(nums), target)
            if key in seen:
                return seen[key]

            # calc recursive relation
            ret = recurse(nums[1:], target - nums[0]) + recurse(
                nums[1:], target + nums[0]
            )
            seen[key] = ret

            return ret

        return recurse(nums, target)
