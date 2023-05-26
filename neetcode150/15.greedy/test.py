from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, end = len(gas) - 1, 0
        total = gas[start] - cost[start]


        while start >= end:
            print(start, end, total)
            while total < 0 and start >= end:
                start -= 1
                total += gas[start] - cost[start]
                print(start, end, total)
            if start == end:
                return start
            total += gas[end] - cost[end]
            end += 1
        
        print("broke out")
        print(start, end)
        return -1


if __name__ == "__main__":
    print(Solution().canCompleteCircuit([0, 0, 0], [3, 3, 3]))
