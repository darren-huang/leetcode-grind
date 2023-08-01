"""2:33pm - 2:55pm"""
from typing import List, Set, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int, end: int) -> Set[Tuple[int, int]]:
        seen = set()
        results = set()
        for i in range(end):
            print(f"    two:{i}, target: {target}")
            n = nums[i]
            if target - n in seen:
                results.add(tuple(sorted([target - n, n])))
            seen.add(n)
        return results

    def threeSum(self, nums: List[int], target: int, end: int) -> Set[Tuple[int, int]]:
        results = set()
        for i in range(end):
            print(f"  three:{i}, target: {target}")
            n = nums[i]
            tSums = self.twoSum(nums, target - n, i)
            results = results.union({tuple(sorted(list(ts) + [n])) for ts in tSums})
        return results

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = set()
        for i in range(len(nums)):
            print(f"four:{i}, target: {target}")
            n = nums[i]
            tSums = self.threeSum(nums, target - n, i)
            results = results.union({tuple(sorted(list(ts) + [n])) for ts in tSums})
        return results
