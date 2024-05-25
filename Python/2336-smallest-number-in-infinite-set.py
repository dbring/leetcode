from heapq import heappush, heappop


class SmallestInfiniteSet:
    def __init__(self):
        """
        SC: O(n) where n is the number of pops
        """

        self.min_heap = [1]
        self.removed = set()

    def popSmallest(self) -> int:
        """
        TC: O(logn) where n is len(self.min_heap)
        """
        smallest = heappop(self.min_heap)
        self.removed.add(smallest)

        if not self.min_heap:
            heappush(self.min_heap, smallest + 1)

        return smallest

    def addBack(self, num: int) -> None:
        """
        TC: O(logn) where n is len(self.min_heap)
        """
        if num in self.removed:
            heappush(self.min_heap, num)
            self.removed.remove(num)
