"""3:27pm - 3:35pm"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        for i in range(len(nums)):
            target = -nums[i]
            seen = {}  # seen -> [index]
            for j in range(i + 1, len(nums)):
                val = nums[j]
                if target - val in seen:
                    # 3 sum found!
                    triplets.add(
                        tuple(sorted([nums[i], nums[j], nums[seen[target - val]]]))
                    )
                else:
                    seen[val] = j

        return list(triplets)