"""9:42am- 10:26am

bad solution look away plz"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] == 0 and nums[i + 1] == 0:
                return True

        curr_sum = 0
        left = 0
        right = 0  # exclusive
        while right < len(nums) and curr_sum < k:
            curr_sum += nums[right]
            right += 1
        if curr_sum < k:
            return False
        if right - left > 1 and curr_sum % k == 0:
            return True

        while True:
            while right < len(nums):
                curr_sum += nums[right]
                right += 1
                if right - left > 1 and curr_sum % k == 0:
                    return True

            if curr_sum < k:
                print(left, right, curr_sum)
                return False

            # decrease window size
            curr_sum -= nums[left]
            left += 1
            if left > len(nums) - 1:
                return False

            if right - left > 1 and curr_sum % k == 0:
                return True
            while curr_sum > k:
                curr_sum -= nums[right - 1]
                right -= 1
                if right - left > 1 and curr_sum % k == 0:
                    return True

            # decrease window size
            curr_sum -= nums[left]
            left += 1
            if left > len(nums) - 1:
                # print(2)
                return False
            if right - left > 1 and curr_sum % k == 0:
                return True
