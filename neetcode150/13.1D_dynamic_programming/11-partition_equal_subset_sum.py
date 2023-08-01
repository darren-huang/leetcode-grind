"""3pm - memoized solution"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        found = False
        total = sum(nums)
        curr = 0
        if total % 2 != 0:
            return False
        memo = {}

        def dfs(i):
            nonlocal curr, found
            # memo
            if (i, curr) in memo:
                return memo[(i, curr)]

            # base case
            if i >= len(nums):
                return curr == total // 2

            n = nums[i]
            if curr + n == total // 2:
                return True
            elif curr + n < total // 2:
                curr += n
                # recurse & memo
                res = dfs(i + 1)
                if res:
                    memo[(i, curr)] = res
                    return res
                curr -= n

            # recurse & memo
            res = dfs(i + 1)
            memo[(i, curr)] = res
            return res

        return dfs(0)
