"""2:21pm
2:26pm

make sure you're USING THE POINTERS CORRECTLY aslkjdf;lkasjdf"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers) - 1
        while p1 < p2:
            sum_ = numbers[p1] + numbers[p2]
            if sum_ == target:
                return [p1 + 1, p2 + 1]
            elif sum_ < target:
                p1 += 1
            else:
                p2 -= 1
        return False
