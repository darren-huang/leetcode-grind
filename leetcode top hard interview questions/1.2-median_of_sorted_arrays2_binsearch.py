"""
Coding time took 35 minutes:

what was slow: 

misconception about the generalized binary search helper
not just a validation function but also needs a direction
had to create an Enum for directions
took too long to think about whether or not it solves the problem correctly


things that could help:

redefine variables to make it more readable
start coding a brute force ugly if-else block, try to clean it up later
define the function, and start working with the given variables, don't think through just start
easier to fix up than thinking it all out



results:
no bugs!!
bit slow
"""
from typing import Any, List
from enum import Enum


class Eq(Enum):
    UP = ("UP",)
    DOWN = ("DOWN",)
    EQ = ("EQ",)


def binary_search_helper(
    sorted_list: List[Any], low: int, high: int, direction_func: callable
) -> Any:
    """Returns the index given the validation function (should return UP DOWN OR EQ)."""
    assert low <= high and low < len(sorted_list) and high < len(sorted_list)

    while low != high:
        mid_index = (low + high) // 2
        direction = direction_func(sorted_list[mid_index])
        if direction == Eq.EQ:
            return sorted_list[mid_index]
        elif direction == Eq.UP:
            low = mid_index + 1
        elif direction == Eq.DOWN:
            high = mid_index - 1

    if direction_func(sorted_list[low]) != Eq.EQ:
        raise ValueError("No valid found")
    return sorted_list[low]


def get_partition(nums1, part1, nums2, part2):
    lower = []
    if part1 > 0:
        lower.append(nums1[part1 - 1])
    if part2 > 0:
        lower.append(nums2[part2 - 1])
    upper = []
    if part1 < len(nums1):
        upper.append(nums1[part1])
    if part2 < len(nums2):
        upper.append(nums2[part2])
    return lower, upper


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # get smaller list
        if len(nums1) <= len(nums2):
            sList, lList = nums1, nums2  # smaller list and larger list
        else:
            sList, lList = nums2, nums1  # smaller list and larger list

        partitions = list(range(0, len(sList) + 1))
        nums_below_median = (len(sList) + len(lList)) // 2

        def direction_func(partition: int) -> Eq:
            # for list x 1 x 2 x 3 x, each x is a valid partition
            sList_part = partition
            lList_part = nums_below_median - sList_part

            # lower slist, upper llist
            if sList_part > 0 and lList_part < len(lList):
                if not (sList[sList_part - 1] <= lList[lList_part]):
                    return Eq.DOWN
            if sList_part < len(sList) and lList_part > 0:
                if not (lList[lList_part - 1] <= sList[sList_part]):
                    return Eq.UP

            return Eq.EQ

        true_sList_part = binary_search_helper(
            partitions, 0, len(sList), direction_func
        )
        true_lList_part = nums_below_median - true_sList_part
        lower, upper = get_partition(sList, true_sList_part, lList, true_lList_part)

        # get median from correct partition
        if (len(sList) + len(lList)) % 2 == 0:  # even case
            return sum([max(lower), min(upper)]) / 2
        else:  # odd case
            return min(upper)


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 2], [3, 4, 5]))
    print(Solution().findMedianSortedArrays([6, 7], [3, 4, 5]))
    print(Solution().findMedianSortedArrays([2, 3], [1, 4, 5]))
