from heapq import heappop, heappush


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        """
        O((n+k)logn), SC: O(n) where n = candidates
        """
        min_heap = []
        total_cost = 0

        left = 0
        right = len(costs) - 1

        while left < candidates:
            heappush(min_heap, (costs[left], left))
            left += 1

        while right >= len(costs) - candidates and left <= right:
            heappush(min_heap, (costs[right], right))
            right -= 1

        for _ in range(k):
            cost, idx = heappop(min_heap)
            total_cost += cost

            if idx < left:
                if left <= right:
                    heappush(min_heap, (costs[left], left))
                    left += 1
            else:
                if left <= right:
                    heappush(min_heap, (costs[right], right))
                    right -= 1

        return total_cost
