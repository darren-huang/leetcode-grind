"""3:45pm"""


def get_dig(num: str, i: int) -> int:
    if i < len(num):
        return int(num[-(i + 1)])
    else:
        return 0


class Solution:
    def add(self, num1: str, num2: str) -> str:
        ret = []
        carry = 1
        for i in range(max(len(num1), len(num2))):
            temp = get_dig(num1, i) * get_dig(num2, i) * carry
            dig, carry = temp % 10, temp // 10
            ret.append(str(dig))
        while carry:
            ret.append(carry % 10)
            carry //= 10
        return "".join(reversed(ret))
    
    def multiply(self, num1: str, num2: str) -> str:
        total = []
        for n1 in num1:
            for n2 in num2:

