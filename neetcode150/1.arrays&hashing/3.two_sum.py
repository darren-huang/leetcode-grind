"""2pm, 2:07pm

remember to clarify input and output"""

from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_indicies = defaultdict(list)
        for i, n in enumerate(nums):
            if target - n in num_to_indicies:
                return [num_to_indicies[target - n][0], i]

            num_to_indicies[n].append(i)
        return False
