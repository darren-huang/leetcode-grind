""""""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]  # a valid combo
        elif target < 0:
            return []  # not a valid combo
        elif len(candidates) == 0:
            return []  # no candidates left

        temp = self.combinationSum(candidates, target - candidates[0])
        used = [[candidates[0]] + combo for combo in temp]
        not_used = self.combinationSum(candidates[1:], target)
        return used + not_used
