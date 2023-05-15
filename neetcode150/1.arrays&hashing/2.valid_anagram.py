"""1:57pm 1:59pm
Done"""

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letter_count = defaultdict(lambda: 0)
        for c in s:
            s_letter_count[c] += 1
        for c in t:
            s_letter_count[c] -= 1
        for _, count in s_letter_count.items():
            if count != 0:
                return False
        return True
