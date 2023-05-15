"""3:11pm
3:44pm

33 min
....

honestly am surprised it worked...
"""

from typing import List


# profit
#         to_buy, to_sell, just_sold
#
#

# x1234321
# 1xO
# 2 x
# 3  x
# 4   xE
# 3    x
# 2     x
# 1      x


# not optimal


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_arr = [[0] * (n) for _ in range(n)]  # [buy][sell]

        def get_cooldown_profit(buy_i):
            if buy_i - 3 >= 0:
                return dp_arr[buy_day_i - 3][buy_day_i - 2]
            return 0

        # initialize array
        for sell_day_i in range(1, n):
            if prices[0] < prices[sell_day_i]:
                dp_arr[0][sell_day_i] = prices[sell_day_i] - prices[0]

        for buy_day_i in range(1, n):
            for sell_day_i in range(n):
                if sell_day_i > buy_day_i:
                    # get sell profit
                    profit = prices[sell_day_i] - prices[buy_day_i]
                    dp_arr[buy_day_i][sell_day_i] = max(
                        dp_arr[buy_day_i - 1][sell_day_i],
                        dp_arr[buy_day_i - 1][sell_day_i - 1],
                        profit + get_cooldown_profit(buy_day_i),
                    )

        return dp_arr[n - 2][n - 1]