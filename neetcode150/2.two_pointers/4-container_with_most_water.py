"""3:51pm - 3:54pm"""
from typing import List

# 1511111111911112


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_seen = 0
        while l < r:
            max_seen = max(min(height[l], height[r]) * (r - l), max_seen)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_seen
