"""7:16pm
badly worded problem, O(n) only possible with count sort which doesn't seem the best
7:33pm going with "quick select"whatever that is

7:49pm done.
"""
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick select
        random.shuffle(nums)

        # setup
        pivot, right_ob = 0, len(nums)  # pointers!!!

        while True:
            prev_pivot, prev_right_ob = pivot, right_ob
            while pivot < right_ob - 1:
                next_i = pivot + 1
                if nums[next_i] < nums[pivot]:
                    nums[next_i], nums[pivot] = nums[pivot], nums[next_i]
                    pivot += 1
                else:
                    right_ob -= 1
                    nums[next_i], nums[right_ob] = nums[right_ob], nums[next_i]

            # now everything to te right of the pivot is gteq
            if len(nums) - pivot == k:
                return nums[pivot]
            elif len(nums) - pivot > k:
                pivot += 1
                right_ob = prev_right_ob
            else:
                pivot = prev_pivot
                right_ob -= 1
