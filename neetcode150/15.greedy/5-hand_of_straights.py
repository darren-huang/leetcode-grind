"""6:10pm - 6:24pm



okay you are tired my friend...
"""

from typing import List
from collections import defaultdict


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort(reverse=True)
        hands = 0
        target_hands = len(hand) // groupSize
        next_card_needed = defaultdict(list)  # (card, [n_more_cards_needed])
        while hand:
            n_card = hand.pop()
            if n_card in next_card_needed:
                # add card to that hand
                cards_left = next_card_needed[n_card].pop()
                cards_left -= 1
                if cards_left:
                    next_card_needed[n_card + 1].append(cards_left)
                if not next_card_needed[n_card]:
                    del next_card_needed[n_card]
            else:
                # add card to new hand
                hands += 1
                next_card_needed[n_card + 1].append(groupSize - 1)

            if hands > target_hands:
                print(next_card_needed)
                return False
        return True
