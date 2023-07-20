"""12:04pm - 12:12pm"""

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = 0
        left, right = 0, 0
        num_valid = 0

        for num in arr:
            # add curr num
            right += 1
            curr_sum += num

            # remove left num if needed
            if right - left > k:
                curr_sum -= arr[left]
                left += 1

            # check window size and avg
            if right - left == k and (curr_sum / (right - left)) >= threshold:
                # print(arr[left: right], curr_sum)
                num_valid += 1
        return num_valid
