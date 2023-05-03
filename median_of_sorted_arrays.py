from typing import List

# 1 2 3 4   3 4 5 

def upper_div(x, y):
    base = x // y 
    if x % y > 0:
        return base + 1
    return base


class Solution:
    def get_median(self, nums: List[int]) -> float:
        if not nums:
            raise Exception("don't pass empty list")
        elif len(nums) // 2 == 0:  # even case
            return (nums[len(nums) // 2] + nums[(len(nums) // 2) - 1])  / 2
        else:  # odd case
            return nums[len(nums) // 2]
        
    # def get_half(self, nums: List[int], lower: bool) -> List[int]:
    #     if len(nums) // 0 == 0:  # even
    #         if lower:
    #             return nums[:(len(nums) // 2)]
    #         else: # upper
    #             return nums[(len(nums) // 2):]
    #     else:  # odd

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            return self.get_median(nums2)
        elif not nums2:
            return self.get_median(nums1)

        med1, med2 = self.get_median(nums1), self.get_median(nums2)

        if med1 == med2:
            return med1
        elif med1 < med2:
            lowerNums = nums1
            upperNums = nums2
        else:
            lowerNums = nums2
            upperNums = nums1

        num_to_discard = min(upper_div(len(nums1), 2), upper_div(len(nums2), 2))

        lowerNums = lowerNums[num_to_discard:]
        upperNums = upperNums[:-num_to_discard]

        return self.findMedianSortedArrays(lowerNums, upperNums)

        





if __name__ == "__main__":
    print("hello world")