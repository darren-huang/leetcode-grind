"""9:59am  - 10:21am

lots of issues...

took like 5-10 to figure out right method

coding out it to be bug free was tricky

lots of branching conditions
!!!!!!!!!
discovery
create a getter function for dp
if i is out of bounds, you can provide the default value
"""


def is_valid(c1, c2):
    if c1 == "0":
        return False
    elif c1 == "1":
        return True
    elif c1 == "2":
        return int(c2) <= 6


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = []  # dp[i] = how many ways to decode s[:i + 1]

        def get_dp(i):
            if i < 0:
                return 1
            return dp[i]

        for i, c in enumerate(s):
            total = 0
            if c != "0":  # treat c as a single
                total += get_dp(i - 1)
            if i > 0 and is_valid(s[i - 1], c):
                total += get_dp(i - 2)
            dp.append(total)
        return dp[-1]
