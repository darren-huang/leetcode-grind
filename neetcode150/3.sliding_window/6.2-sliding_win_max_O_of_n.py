"""2:15pm - 2:27pm


trick for max
upper bound
or maintain a monotonically increasing queue


bug: keep track of index vs value
"""

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return [max(nums)]

        window_q = deque()  # holds index where it goes greatest -> least
        max_window_ret = []

        for i in range(len(nums)):
            while window_q and nums[window_q[-1]] < nums[i]:
                window_q.pop()
            window_q.append(i)

            if window_q[0] < i - k + 1:
                window_q.popleft()

            if i >= k - 1:
                max_window_ret.append(nums[window_q[0]])

        return max_window_ret