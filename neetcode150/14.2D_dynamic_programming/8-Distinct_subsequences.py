"""10:24am- 10:44am"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # recursive relation
        # f(s[:i+1], t[:j+1]) =
        #  if s[i] == t[j]:
        #       += f(s[:i], t[:j])
        #  += f(s[:i], t[:j+1])
        dp_curr = [1] * len(s)

        def get(i, j, arr):
            if i < 0:
                if j < 0:
                    return 1
                else:
                    return 0
            else:
                return arr[i]

        for j in range(len(t)):
            dp_next = [0] * len(s)
            for i in range(len(dp_next)):
                dp_next[i] += get(i - 1, j, dp_next)
                if s[i] == t[j]:
                    dp_next[i] += get(i - 1, j - 1, dp_curr)
            dp_curr = dp_next
        return dp_curr[-1]
