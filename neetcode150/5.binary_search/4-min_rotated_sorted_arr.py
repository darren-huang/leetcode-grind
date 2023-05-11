"""12:33pm - 12:44pm

check boundaries
check returns
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l_i, r_i = 0, len(nums) - 1
        while l_i < r_i:
            m_i = (l_i + r_i) // 2
            if nums[m_i - 1] > nums[m_i]:
                # correct split, m_i is answer
                return nums[m_i]
            elif nums[m_i] < nums[-1]:
                # m_i to the end, are in sorted order
                r_i = m_i - 1
            else:
                l_i = m_i + 1
        return nums[l_i]