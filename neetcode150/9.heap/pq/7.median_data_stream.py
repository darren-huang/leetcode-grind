"""6:20 - 6:30pm

bit trickier than i thought

had to realize that for the upper bits that you'd need to move items between the two
"""
import heapq


class MedianFinder:
    def __init__(self):
        self.lower_half = []  # max heap ALL ITEMS ARE NEGATIVE
        self.upper_half = []  # min heap

    def addNum(self, num: int) -> None:
        if len(self.lower_half) < len(self.upper_half):
            heapq.heappush(self.lower_half, -num)
        else:
            heapq.heappush(self.upper_half, num)

        if self.lower_half and self.upper_half:
            while self.upper_half[0] < -self.lower_half[0]:
                temp_lower, temp_upper = -heapq.heappop(self.lower_half), heapq.heappop(
                    self.upper_half
                )
                heapq.heappush(self.lower_half, -temp_upper)
                heapq.heappush(self.upper_half, temp_lower)

    def findMedian(self) -> float:
        if len(self.lower_half) == len(self.upper_half):
            # case where even number of items
            return (-self.lower_half[0] + self.upper_half[0]) / 2
        else:
            # case with odd, upper half always has more
            return self.upper_half[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
