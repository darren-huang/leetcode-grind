"""2:47pm, 2:51pm"""


class Solution:
    def isValid(self, s: str) -> bool:
        paren_stack = []
        paren_match = {"{": "}", "(": ")", "[": "]"}

        for paren in s:
            if paren in ["{", "[", "("]:  # open paren
                paren_stack.append(paren)
            else:  # close paren
                if not paren_stack:
                    return False
                if not paren_match[paren_stack.pop()] == paren:
                    return False
        return len(paren_stack) == 0
