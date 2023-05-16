"""3:55pm - 4:16pm


clever way of keeping track of the max

->
instead of keeping a running track of max
just keep track of upper bound ->


"""
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_seen = 0
        chars = set(s)
        for c in chars:
            num_c = 0
            num_chars = 0
            for i in range(len(s)):
                # update counts
                num_chars += 1
                if s[i] == c:
                    num_c += 1

                # update back pointer
                while num_chars - num_c > k:
                    num_chars -= 1
                    if s[i - (num_chars - 1)] == c:
                        num_c -= 1
                
                # update_max
                max_seen = max(max_seen, num_chars)
        return max_seen

