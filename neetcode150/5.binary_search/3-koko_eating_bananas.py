"""did lots of distractions
but...
took way too long
probably like 40 minutes"""

import heapq

from typing import List


def hr_count(pile, k):
    if k == 0:
        return float("infinity")
    return pile // k + (0 if pile % k == 0 else 1)


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        num_extra = h - len(piles)
        if num_extra == 0:
            return max(piles)

        # get top num_extra
        top_most = heapq.nlargest(num_extra + 1, piles)
        top_most = sorted(top_most)

        low_k, high_k = 0, max(top_most)
        new_h = h - (len(piles) - len(top_most))

        while low_k < high_k:
            mid_k = (low_k + high_k) // 2
            print(mid_k)
            hr_count1 = sum([hr_count(p, mid_k) for p in top_most])
            hr_count2 = sum([hr_count(p, mid_k + 1) for p in top_most])
            if hr_count1 > new_h and hr_count2 <= new_h:
                # found correct
                return mid_k + 1
            elif hr_count1 > new_h and hr_count2 > new_h:
                # both too slow, need bigger k
                low_k = mid_k + 1
            else:
                high_k = mid_k - 1

        if low_k == high_k:
            return low_k + 1
        return False
