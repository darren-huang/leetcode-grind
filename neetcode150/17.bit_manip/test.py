class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask in hexadecimal
        mask = 0xFFFFFFFF

        # works both as while loop and single value check
        while (b & mask) > 0:
            print(bin(a), bin(b))

            carry = (a & b) << 1
            a = a ^ b
            b = carry

        # handles overflow
        print(bin(a), bin(b))
        return (a & mask) if b > 0 else a


if __name__ == "__main__":
    print(Solution().getSum(-1, -1))
