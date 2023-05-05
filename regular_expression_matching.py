"""start 12:47pm
1:02pm
solution timed out

1:20pm
added cached solution
fixed time out issue


"""


def match_char(c1, p1):
    if p1 == ".":
        return True
    return c1 == p1


class Solution:
    cache = {}

    def isMatch(self, s: str, p: str) -> bool:
        self.cache = {}
        return self.isMatchHelperCached(s, p)

    def isMatchHelperCached(self, s: str, p: str) -> bool:
        if (s, p) in self.cache:
            return self.cache[(s, p)]
        result = self.isMatchHelper(s, p)
        self.cache[(s, p)] = result
        return result

    def isMatchHelper(self, s: str, p: str) -> bool:
        if len(p) >= 2 and p[0] != "*" and p[1] == "*":  # asterisk case
            if self.isMatchHelperCached(s, p[2:]):
                return True
            for i in range(len(s)):
                c = s[i]  # ith character
                if match_char(c, p[0]):  # if match, then CAN discard
                    if self.isMatchHelperCached(s[i + 1 :], p[2:]):
                        return True
                else:
                    break
            return False
        else:  # normal case
            if not s:
                if not p:
                    return True
                else:
                    return False
            else:  # s exists
                if not p:
                    return False
                else:
                    if match_char(s[0], p[0]):
                        return self.isMatchHelperCached(s[1:], p[1:])
                    else:
                        return False


if __name__ == "__main__":
    print(Solution().isMatch("aa", "a*"))
