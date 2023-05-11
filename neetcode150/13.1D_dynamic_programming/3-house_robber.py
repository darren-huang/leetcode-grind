"""9:19pm

2 mistakes

didn't max l3,l2,l1
used nums[-1] instead of nums[2]



------
"faster solutions"
instead dp_arr[i] representing Max money IFF we rob house i
dp_arr[i] represents Max money considering houses up to (and including) house i

didn't take too long
like 7 min? lost track
"""

from typing import List

# [1, 2, 3, 4]
# 1 2 4 6


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        # each reps the max if you rob the last i'th house
        l3, l2, l1 = nums[0], nums[1], nums[0] + nums[2]
        for i in range(3, len(nums)):
            l0 = max(l3, l2) + nums[i]
            l3, l2, l1 = l2, l1, l0

        return max(l3, l2, l1)
