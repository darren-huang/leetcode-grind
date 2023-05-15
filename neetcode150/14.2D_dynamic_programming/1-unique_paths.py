"""2:41pm - 2:45pm"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_arr = [1] * m
        for _ in range(n):
            for j in range(1, m):
                dp_arr[j] = dp_arr[j - 1] + dp_arr[j]
        return dp_arr[-1]
