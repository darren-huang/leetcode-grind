"""4:34pm"""

from typing import List
from collections import deque


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        curr_permutation = [None] * len(nums)
        temp_nums = deque(nums.copy())

        def dfs(i):
            if i >= len(curr_permutation):
                permutations.append(curr_permutation.copy())

            for _ in range(len(temp_nums)):
                curr_permutation[i] = temp_nums.popleft()
                dfs(i + 1)
                temp_nums.append(curr_permutation[i])

        dfs(0)
        return permutations
