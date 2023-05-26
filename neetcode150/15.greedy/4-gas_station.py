"""5:28pm"""
from typing import List
from collections import deque


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas = deque(gas)
        cost = deque(cost)

        curr_answer = 0
        seen = 0
        n = len(gas)
        while gas and seen < n:
            total = 0
            while gas and total >= 0:
                total += gas.popleft()
                total -= cost.popleft()
                seen += 1
            gas.append(0)
            cost.append(-total)
            curr_answer = seen + 1
        
        if not gas:
            return curr_answer
        else:
            return -1
