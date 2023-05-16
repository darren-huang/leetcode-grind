"""12:28pm - 12:47pm"""


class Solution:
    def reverse(self, x: int) -> int:
        min_, max_ = -(2**31), 2**31 - 1
        ret = 0
        divisor = 10
        is_negative = False
        if x < 0:
            divisor = -10
            is_negative = True

        while x:
            digit = x % divisor
            x = x // divisor
            if is_negative:
                x = -x
                if ret < -((min_ - digit) // -10):
                    return 0
            else:
                if ret > (max_ - digit) // 10:
                    return 0

            ret = ret * 10 + digit
        return ret
