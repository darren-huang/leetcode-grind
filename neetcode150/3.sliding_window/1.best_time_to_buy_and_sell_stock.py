"""2:32pm, 2:34pm done"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float("-infinity")
        min_price = float("infinity")
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
        return max(0, max_profit)
