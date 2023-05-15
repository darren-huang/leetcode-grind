"""5:42pm
5:48pm
"""

from typing import List
from collections import defaultdict


def get_counts(nums):
    counts = defaultdict(lambda: 0)
    for n in nums:
        counts[n] += 1
    return counts


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # get count
        counts = get_counts(nums)
        num_and_count = list(counts.items())

        # backtrack
        ret_subsets = []
        subset = []

        def dfs(i):
            if i >= len(num_and_count):
                ret_subsets.append(subset.copy())
                return

            num, count = num_and_count[i]
            for _ in range(count):
                subset.append(num)
                dfs(i + 1)
            for _ in range(count):
                subset.pop()
            dfs(i + 1)

        dfs(0)
        return ret_subsets
