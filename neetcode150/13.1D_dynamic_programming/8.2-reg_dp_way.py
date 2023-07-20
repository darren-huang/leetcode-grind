from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + ([-1] * amount)  # dp[price] = min coins

        for price in range(amount):
            if dp[price] == -1:
                continue
            cc = dp[price] + 1  # coin count
            for c in coins:
                n_price = c + price
                if n_price > amount:
                    continue
                dp[n_price] = cc if dp[n_price] == -1 else min(cc, dp[n_price])

        return dp[amount]
