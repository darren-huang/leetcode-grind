"""1:46pm- 1:53pm"""
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = defaultdict(lambda: 0)
        for c in s1:
            s1_count[c] += 1

        def clean(c):
            if not s1_count[c]:
                del s1_count[c]

        num_letters = 0
        for i in range(len(s2)):
            # update counts
            c = s2[i]
            s1_count[c] -= 1
            clean(c)
            num_letters += 1
            if num_letters > len(s1):
                rm_c = s2[i - len(s1)]
                s1_count[rm_c] += 1
                clean(rm_c)

            # check permutation
            if not s1_count:
                return True

        return False
