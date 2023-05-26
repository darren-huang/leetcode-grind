"""9:34am - 9:50am"""

from typing import List


def overlap(s1, e1, s2, e2):
    return not (e1 < s2 or e2 < s1)


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        ret_intervals = []
        n_start, n_end = newInterval
        merged = False
        for start, end in intervals:
            if overlap(n_start, n_end, start, end):
                n_start, n_end = min(start, n_start), max(end, n_end)
            elif n_end < start and not merged:
                ret_intervals.append([n_start, n_end])
                ret_intervals.append([start, end])
                merged = True
            else:
                ret_intervals.append([start, end])
        if not merged:
            ret_intervals.append([n_start, n_end])
        return ret_intervals
