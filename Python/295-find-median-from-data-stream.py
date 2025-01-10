import heapq


class MedianFinder:
    def __init__(self):
        self.low = []  # max heap
        self.high = []  # min heap

    def addNum(self, num: int) -> None:
        """
        TC: O(log n), SC: O(1)
        """
        heapq.heappush(self.low, -1 * num)
        max_element = heapq.heappop(self.low)
        heapq.heappush(self.high, -1 * max_element)

        if len(self.low) < len(self.high):
            min_element = heapq.heappop(self.high)
            heapq.heappush(self.low, -1 * min_element)

    def findMedian(self) -> float:
        """
        TC: O(1), SC: O(1)
        """
        if len(self.high) == len(self.low):
            return (self.high[0] - self.low[0]) / 2

        return -1 * self.low[0]
