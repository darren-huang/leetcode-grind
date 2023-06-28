"""start 11:53am - 12:02"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = []  # max considering nums[:i + 1]
        dp_min = []  # min considering nums[:i + 1]
        for n in nums:
            if dp_max and dp_min:
                n2, n3 = dp_max[-1] * n, dp_min[-1] * n
                dp_max.append(max(n, n2, n3))
                dp_min.append(min(n, n2, n3))
            else:
                dp_max.append(n)
                dp_min.append(n)
        return max(dp_max)
