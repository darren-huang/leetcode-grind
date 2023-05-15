"""did lots of distractions
but...
took way too long
probably like 40 minutes"""

from typing import List


def get_hrs(pile, k):
    if k == 0:
        return float("infinity")
    return pile // k + (0 if pile % k == 0 else 1)


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low_k, high_k = 1, max(piles)

        while low_k < high_k:
            mid_k = (low_k + high_k) // 2
            total_hrs = sum([get_hrs(p, mid_k) for p in piles])
            last_total_hrs = sum([get_hrs(p, mid_k - 1) for p in piles])

            if last_total_hrs > h and total_hrs <= h:
                # correct interval
                return mid_k
            elif last_total_hrs > h and total_hrs > h:
                # both are taking too long
                low_k = mid_k + 1
            else:
                high_k = mid_k - 1

        return low_k
