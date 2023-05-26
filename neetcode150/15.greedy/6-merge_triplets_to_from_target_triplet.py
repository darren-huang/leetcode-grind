"""10:15am - 10:21"""
from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        targets_left = set(enumerate(target))
        for triplet in triplets:
            for i, itarget in list(targets_left):
                if triplet[i] == itarget:
                    all_lte = all([trip <= targ for trip, targ in zip(triplet, target)])
                    if all_lte:
                        targets_left.remove((i, itarget))

        return len(targets_left) == 0
