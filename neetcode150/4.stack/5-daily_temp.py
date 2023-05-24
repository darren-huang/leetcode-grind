"""2:28pm - 2:33pm"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waiting_for_warmer = []  # holds INDEX
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while waiting_for_warmer and temperatures[waiting_for_warmer[-1]] < temp:
                ans[waiting_for_warmer[-1]] = i - waiting_for_warmer[-1]
                waiting_for_warmer.pop()

            waiting_for_warmer.append(i)

        return ans
