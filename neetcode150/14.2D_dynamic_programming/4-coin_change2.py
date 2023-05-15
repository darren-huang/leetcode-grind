"""4:00pm - 4:10pm"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        seen = {}

        def get_change(amount, coins):
            if (amount, tuple(coins)) in seen:
                return seen[(amount, tuple(coins))]

            # base case
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            if not coins:
                return 0

            use_ways = get_change(amount - coins[-1], coins)  # use coin
            dont_use_ways = get_change(amount, coins[:-1])  # don't use coin
            ret = use_ways + dont_use_ways
            seen[(amount, tuple(coins))] = ret
            return ret

        return get_change(amount, coins)