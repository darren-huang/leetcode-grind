"""6:33pm 6:43 with some girlfriend intermission

base case was tricky
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        next_subsets = self.subsets(nums[1:])
        num = nums[0]
        return [[num] + arr for arr in next_subsets] + next_subsets
