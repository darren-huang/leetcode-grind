""""""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret_subsets = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                ret_subsets.append(subset.copy())
                return

            # add i-th item
            subset.append(nums[i])
            dfs(i + 1)

            # don't add i-th item
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return ret_subsets
