"""3:10pm

3:40pm"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]  # a valid combo
        elif target < 0:
            return []  # not a valid combo
        elif len(candidates) == 0:
            return []  # no candidates left

        used = []
        n_used = 1
        while target - (candidates[0] * n_used) >= 0:
            new_target = target - (candidates[0] * n_used)
            temp_combos = self.combinationSum(candidates[1:], new_target)
            used.extend([([candidates[0]] * n_used) + combo for combo in temp_combos])
            n_used += 1

        not_used = self.combinationSum(candidates[1:], target)
        return used + not_used
