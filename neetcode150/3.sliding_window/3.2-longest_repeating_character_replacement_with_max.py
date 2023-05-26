"""4:30pm - 4:33pm
"""
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(lambda: 0)
        l, max_seen, upper_bound_freq = 0, 0, 0
        for r in range(len(s)):
            count[s[r]] += 1
            upper_bound_freq = max(upper_bound_freq, count[s[r]])

            # check if num letters, minus highest frequency letter (ie. num replacements neede)
            if (r - l + 1) - upper_bound_freq > k:
                count[s[l]] -= 1
                l += 1

            # update max_seen
            max_seen = max(max_seen, (r - l + 1))

        return max_seen
