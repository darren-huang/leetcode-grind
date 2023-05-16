"""11:02am-11:10am"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for n in nums:
            num = num ^ n
        return num
