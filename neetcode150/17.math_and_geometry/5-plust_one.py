"""3:36pm - 3:40pm"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result: List[int] = []
        carry = 1
        for dig in digits[::-1]:
            temp = dig + carry
            dig, carry = temp % 10, temp // 10
            result.append(dig)
        head = [] if not carry else [1]
        return head + list(reversed(result))
