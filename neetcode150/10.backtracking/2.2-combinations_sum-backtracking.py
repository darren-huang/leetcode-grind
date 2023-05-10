""""""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret_combos = []

        subset = []

        def dfs(i, temp_sum):
            """Use the i'th candidate n times"""
            if temp_sum == target:
                ret_combos.append(subset.copy())
                return
            elif temp_sum > target:
                return
            elif i >= len(candidates):
                return

            subset.append(candidates[i])
            dfs(i, temp_sum + candidates[i])
            subset.pop()
            dfs(i + 1, temp_sum)

        dfs(0, 0)
        return ret_combos
