import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    print(i, minH)
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True


if __name__ == "__main__":
    print(Solution().isNStraightHand([1, 2, 3, 1, 2, 3], 3))
