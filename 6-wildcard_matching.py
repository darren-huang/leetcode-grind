"""Cached solution
5-10 minutes

doesn't pass time requirements tho (runtime)

"""


def cache_decorator(func):
    cache = {}

    def cached_func(*args, **kwargs):
        key = (tuple(args), tuple(kwargs.items()))
        if key in cache:
            return cache[key]
        ret_val = func(*args, **kwargs)
        cache[key] = ret_val
        return ret_val

    return cached_func


class Solution:
    @cache_decorator
    def isMatch(self, s: str, p: str) -> bool:
        """only ? and * characters"""
        if not p:  # No Pattern left to check
            if not s:
                return True
            else:
                return False

        if not s:  # No String left to check
            if p[0] == "*":
                return self.isMatch(s, p[1:])
            else:
                return False

        if p[0] == "*":
            if self.isMatch(s[1:], p):  # remove 1 char, keep *
                return True
            if self.isMatch(s, p[1:]):  # remove 0 char, remove *
                return True
            return False
        elif p[0] == "?" or p[0] == s[0]:
            return self.isMatch(s[1:], p[1:])
        else:
            return False
