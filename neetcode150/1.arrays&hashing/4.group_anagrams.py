"""2:08pm

2:11pm


found a faster solution to just sort the words
"""

from typing import List
from collections import defaultdict


def get_letter_count(word: str):
    counts = defaultdict(lambda: 0)
    for c in word:
        counts[c] += 1
    return counts


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)  # counts tuple to set
        for str in strs:
            counts = get_letter_count(str)
            key = tuple(sorted(counts.items()))
            groups[key].append(str)
        return list(groups.values())
