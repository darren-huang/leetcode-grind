"""3:40 - 3:44pm"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n < 0:
            x = 1 / x
            n = -n
        while n > 0:
            if n % 2 == 1:
                result *= x
                n -= 1
            else:  # even
                x *= x
                n //= 2
        return result
