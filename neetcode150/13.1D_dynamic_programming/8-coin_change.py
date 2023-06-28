from collections import defaultdict
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_price = 0
        price_to_num_coins = {0: 0}
        seen = set([0])
        while min_price < amount and amount not in price_to_num_coins:
            min_price = float("inf")
            nxt_price_to_num_coins = defaultdict(lambda: float("inf"))
            for price, n_coins in price_to_num_coins.items():
                for c in coins:
                    if price + c not in seen:
                        nxt_price_to_num_coins[price + c] = min(
                            nxt_price_to_num_coins[price + c], n_coins + 1
                        )
                        min_price = min(min_price, price + c)
            for price in nxt_price_to_num_coins:
                seen.add(price)
            price_to_num_coins = nxt_price_to_num_coins

        if amount in price_to_num_coins:
            return price_to_num_coins[amount]
        return -1
