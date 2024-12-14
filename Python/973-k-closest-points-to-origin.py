import heapq
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        TC: O(n*logk) SC: O(k) where n = len(points)
        """
        ORIGIN = [0, 0]
        max_heap = []

        def distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2

            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        for point in points:
            dist = distance(point, ORIGIN)
            heapq.heappush(max_heap, (-dist, point))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [point for _, point in max_heap]

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Quickselect
        TC: O(n) on average, O(n^2) worst case
        SC: O(1)
        """
        import math
        import random

        ORIGIN = [0, 0]

        def distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2

            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        def swap(i, j):
            points[i], points[j] = points[j], points[i]
            return

        def partition(left, right):
            pivot_idx = random.randint(left, right)
            pivot_number = distance(points[pivot_idx], ORIGIN)
            swap(pivot_idx, right)
            partition_idx = left

            for i in range(left, right):
                if distance(points[i], ORIGIN) <= pivot_number:
                    swap(i, partition_idx)
                    partition_idx += 1

            swap(partition_idx, right)
            return partition_idx

        def quickselect(left, right):
            while left <= right:
                p = partition(left, right)

                if p < k:
                    left = p + 1
                else:
                    right = p - 1

            return points[:k]

        return quickselect(0, len(points) - 1)
