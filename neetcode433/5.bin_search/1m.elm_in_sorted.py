"""10:13am 10:22am """
from typing import List


def inbounds(i, length):
    return 0 <= i and i < length


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            corresponding = m + 1 if m % 2 == 0 else m - 1
            other = m - 1 if m % 2 == 0 else m + 1
            if inbounds(corresponding, len(nums)) and nums[m] == nums[corresponding]:
                # ordering is correct on the left side, right side contains nondup
                l = m + 1
            else:
                if inbounds(other, len(nums)) and nums[m] == nums[other]:
                    r = m - 1
                else:
                    return nums[m]
        return -1
