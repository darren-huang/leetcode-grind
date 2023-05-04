"""Notes:

This is the initial thought for the problem

if you compare the medians of the 2 arrays you can somehow figure out which halves to discard

this is correct but takes some more indepth thinking to get the base case
In practice the base case is really annoying due to the added issues of even vs odd
as well as varying possibilities.

Essentially in general if median1 is < median2
then the lower half of nums1 can be discarded 
and the upper half of nums2 can be discarded

an important caveat which tripped me up was that
if a list has a even number of numbers, you CAN'T discard the middle 2 elements
these are always possible to contribute the final true median

knowing this the base case must be when you have an array of 2 or less since it will 
never be smaller than this. Handling the base case is figuring out the quickest method
to find the median of a long sorted list + 1 or 2 numbers.

Dumb mistakes to look out for:

// vs % when checking even vs. odd
variable names inside each function
"""
from typing import List

class Solution:
    def get_num_to_discard(self, nums: List[int]) -> int:
        return (len(nums) - 1) // 2

    def get_median(self, nums: List[int]) -> float:
        if not nums:
            raise Exception("don't pass empty list")
        elif len(nums) % 2 == 0:  # even case
            return (nums[len(nums) // 2] + nums[(len(nums) // 2) - 1]) / 2
        else:  # odd case
            return nums[len(nums) // 2]

    def get_middle(self, nums: List[int]) -> List[int]:
        """If even, get middle 2, if odd get middle 3."""
        if len(nums) <= 4:
            return nums
        elif len(nums) % 2 == 0:  # even case
            return [
                nums[len(nums) // 2],
                nums[(len(nums) // 2) - 1],
                nums[(len(nums) // 2) - 2],
                nums[(len(nums) // 2) + 1],
            ]
        else:  # odd case
            return [
                nums[len(nums) // 2],
                nums[(len(nums) // 2) - 1],
                nums[(len(nums) // 2) + 1],
            ]

    def handle_base_case(self, fewerNums: List[int], nums2: List[int]) -> float:
        if len(fewerNums) == 0:
            return self.get_median(nums2)
        return self.get_median(sorted(self.get_middle(nums2) + fewerNums))

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= 2:
            return self.handle_base_case(nums1, nums2)
        elif len(nums2) <= 2:
            return self.handle_base_case(nums2, nums1)

        med1, med2 = self.get_median(nums1), self.get_median(nums2)

        if med1 == med2:
            return med1
        elif med1 < med2:
            lowerNums = nums1
            upperNums = nums2
        else:
            lowerNums = nums2
            upperNums = nums1

        num_to_discard = min(
            self.get_num_to_discard(lowerNums), self.get_num_to_discard(upperNums)
        )

        lowerNums = lowerNums[num_to_discard:]
        upperNums = upperNums[:-num_to_discard]

        return self.findMedianSortedArrays(lowerNums, upperNums)


# if __name__ == "__main__":
#     Solution().findMedianSortedArrays([1, 2], [3, 4])
