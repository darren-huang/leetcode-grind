"""8:57pm - 9:01pm"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        last2, last1 = 1, 2
        for _ in range(n - 2):
            last2, last1 = last1, last1 + last2

        return last1
