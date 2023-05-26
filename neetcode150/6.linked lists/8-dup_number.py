"""11:22am - 11:31am"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]

            # keep replacing numbers to their correct spot
            while n - 1 != i:
                new_n = nums[n - 1]

                # check condition
                if new_n == n:
                    return n

                # swap
                nums[n - 1], nums[i] = nums[i], nums[n - 1]
                n = nums[i]

        return False
