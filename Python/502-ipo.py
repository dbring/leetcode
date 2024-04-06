class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: list[int], capital: list[int]
    ) -> int:
        """
        TC: O(nlogn), SC:O(n) where n = len(profits)
        """
        from heapq import heappush, heappop

        n = len(profits)
        max_heap = []

        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort(key=lambda x: x[0])

        for _ in range(k):
            while projects and projects[0][0] <= w:
                profit = projects.pop(0)[1]
                heappush(max_heap, -profit)

            if not max_heap:
                break

            w += -heappop(max_heap)

        return w
