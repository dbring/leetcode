from heapq import heappush, heappop


class Solution:
    def kSmallestPairs(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> list[list[int]]:
        """
        TC: O(min(klogk, mnlogmn)), SC: O(min(k, mn))
        """
        m = len(nums1)
        n = len(nums2)
        visited = set()
        k_smallest_pairs = []

        min_heap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))

        # BFS
        for _ in range(min(k, m * n)):
            _, (i, j) = heappop(min_heap)

            k_smallest_pairs.append([nums1[i], nums2[j]])

            # Add both possible neighbors
            if i + 1 < m and (i + 1, j) not in visited:
                heappush(min_heap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heappush(min_heap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))

        return k_smallest_pairs
