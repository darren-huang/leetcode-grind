"""4:34pm"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        curr_permutation = [None] * len(nums)
        positions = set(range(len(nums)))

        def dfs(i):
            if i >= len(nums):
                permutations.append(curr_permutation.copy())

            for pos in list(positions):
                curr_permutation[pos] = nums[i]
                positions.remove(pos)
                dfs(i + 1)
                positions.add(pos)
        
        dfs(0)
        return permutations
            
