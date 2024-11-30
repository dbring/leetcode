from heapq import nsmallest, nlargest


class Solution:
    def minDifference(self, nums: list[int]) -> int:
        """
        TC: O(n), SC: O(1) where n = len(nums)
        """
        if len(nums) <= 4:
            return 0

        smallest_four = sorted(nsmallest(4, nums))

        largest_four = sorted(nlargest(4, nums))

        min_diff = float("inf")

        for i in range(4):
            min_diff = min(min_diff, largest_four[i] - smallest_four[i])

        return min_diff
