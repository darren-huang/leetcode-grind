"""10:59am - 11:01am"""


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            temp_sum = 0
            while n > 0:
                temp_sum += (n % 10) ** 2
                n = n // 10
            n = temp_sum
        return n == 1
