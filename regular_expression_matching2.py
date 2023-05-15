"""better memoization method

using cache_decorator
works as expected
"""


def match_char(c1, p1):
    if p1 == ".":
        return True
    return c1 == p1

def cache_decorator(func):
    cache = {}
    def cached_func(*args, **kwargs):
        key = (tuple(args), tuple(kwargs.items()))
        if key in cache:
            return cache[key]
        ret = func(*args, **kwargs)
        cache[key] = ret
        return ret
    return cached_func

class Solution:
    cache = {}

    @cache_decorator
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) >= 2 and p[0] != "*" and p[1] == "*":  # asterisk case
            if self.isMatch(s, p[2:]):
                return True
            for i in range(len(s)):
                c = s[i]  # ith character
                if match_char(c, p[0]):  # if match, then CAN discard
                    if self.isMatch(s[i + 1 :], p[2:]):
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
                        return self.isMatch(s[1:], p[1:])
                    else:
                        return False


if __name__ == "__main__":
    print(Solution().isMatch("aaaaaaa", "a*aa*aa*a"))
