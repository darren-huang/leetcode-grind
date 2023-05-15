"""2:57pm"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_p, end_p = 0, len(nums) - 1
        while start_p < end_p:
            middle_p = (start_p + end_p) // 2
            middle_val = nums[middle_p]
            if middle_val == target:
                return middle_p
            elif middle_val < target:
                start_p = middle_p + 1
            elif middle_val > target:
                end_p = middle_p - 1
        return -1


if __name__ == "__main__":
    print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
