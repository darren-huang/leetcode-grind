"""2:28pm - 2:33pm"""
from typing import List
from collections import defaultdict


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # get the count 
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        # overwrite arr
        pointer = 0
        for i in range(3):
            for _ in range(count[i]):
                nums[pointer] = i
                pointer += 1






