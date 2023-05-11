"""10:29am

10:53am

changing the represenation of the items is a messy slope
ie. storing tuples of operand and number


also
easiest method
is to iterate from the left, not the right....
"""

from typing import List

OPERANDS = {
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
}


def is_num(char):
    return char not in OPERANDS


def is_operand(char):
    return char in OPERANDS


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        while tokens:
            next_token = tokens.pop()
            if next_token in OPERANDS:
                stack.append(OPERANDS)
            else:  # is number
                num = next_token
                while stack and is_num(stack[-1]) and is_operand(stack[-2]):
                    num1, op = stack.pop(), stack.pop()
                    num = OPERANDS[op](num1, num)
                stack.append(num)
        return stack[0]
