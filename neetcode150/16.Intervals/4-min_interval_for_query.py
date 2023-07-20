"""11:16am

TRY SORTING BOTH
"""
from typing import List
import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        intervals_heap = []  # (size, start, end)
        answers = {}  # q: min interval size of q
        i = 0

        for q in sorted(queries):
            # add to heap, all intervals with valid starts
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i]
                heapq.heappush(intervals_heap, (e - s + 1, s, e))
                i += 1

            # remove from heap all intervals with invalid ends
            while intervals_heap and intervals_heap[0][2] < q:
                heapq.heappop(intervals_heap)

            answers[q] = -1 if not intervals_heap else intervals_heap[0][0]

        return [answers[q] for q in queries]
