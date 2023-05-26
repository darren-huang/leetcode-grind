"""11:11am - 11:15am"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n > 0:
            ret += n & 1
            n = n >> 1
        return ret