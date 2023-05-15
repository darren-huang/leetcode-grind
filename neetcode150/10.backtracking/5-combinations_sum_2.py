"""8:18pm
8:28pm

no mistakes, could be faster tho"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ret_combos = []
        curr_combo = []

        def dfs(i, total):
            # base case based off of total and i, value
            if target == total:
                ret_combos.append(curr_combo.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # get number of repeated current values (updates i)
            curr_val = candidates[i]
            count = 1
            while i + 1 < len(candidates) and curr_val == candidates[i + 1]:
                i += 1
                count += 1

            for j in range(count):
                curr_combo.append(curr_val)
                dfs(i + 1, total + (curr_val * (j + 1)))
            for _ in range(count):
                curr_combo.pop()
            dfs(i + 1, total)  # do not use current val, total isn't changed

        dfs(0, 0)
        return ret_combos
