from heapq import heappush, heappop


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """
        TC: O(nlogn), SC:O(n) where n = len(nums1) due to sorting.
        """
        max_score = float("-inf")
        min_heap = []
        current_sum = 0
        nums = [(nums2[i], nums1[i]) for i in range(len(nums1))]
        nums.sort(reverse=True)

        for n2, n1 in nums:
            current_sum += n1
            heappush(min_heap, n1)

            if len(min_heap) > k:
                current_sum -= heappop(min_heap)

            if len(min_heap) == k:
                max_score = max(max_score, current_sum * n2)

        return max_score
