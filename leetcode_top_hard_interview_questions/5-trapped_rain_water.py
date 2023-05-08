"""4:35pm
finish 4:50pm

mistakes: incremented one of the indices wrong


things to check
BASE CASE!!!
INCREMENTATION!!!
RETURNS!!!
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left_max = height[0]
        right_max = height[-1]
        left_index = 0
        right_index = len(height) - 1

        while left_index != right_index:
            # figure out which side to increment
            if left_max <= right_max:
                # increment left
                left_index += 1
                new_val = height[left_index]
                if new_val <= left_max:
                    total += left_max - new_val
                else:
                    left_max = new_val
            else:
                # increment right
                right_index -= 1
                new_val = height[right_index]
                if new_val <= right_max:
                    total += right_max - new_val
                else:
                    right_max = new_val
        if height[left_index] < min(left_max, right_max):
            total += min(left_max, right_max) - height[left_index]
        
        return total


