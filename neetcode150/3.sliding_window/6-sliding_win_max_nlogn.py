"""1:54pm - 2:05pm"""

from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return [max(nums)]

        window = set()  # holds indices
        max_heap = (
            []
        )  # remeber that these vals are NEGATIVE (max heap)  holds (-priority, index)
        max_window_ret = []

        for i in range(len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))
            window.add(i)

            if len(window) > k:
                rm_i = i - k
                window.remove(rm_i)

            if len(window) == k:
                while max_heap[0][1] not in window:
                    heapq.heappop(max_heap)
                max_window_ret.append(-max_heap[0][0])
        
        return max_window_ret
