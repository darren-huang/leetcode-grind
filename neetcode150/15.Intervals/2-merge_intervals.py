"""10:00am - 10:06am"""

from typing import List


def overlap(s1, e1, s2, e2):
    return not (e1 < s2 or e2 < s1)


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort()
        ret = []

        c_start, c_end = intervals[0]
        for start, end in intervals[1:]:
            if overlap(c_start, c_end, start, end):
                c_start, c_end = min(c_start, start), max(c_end, end)
            else:
                ret.append([c_start, c_end])
                c_start, c_end = start, end
        ret.append([c_start, c_end])
        return ret
