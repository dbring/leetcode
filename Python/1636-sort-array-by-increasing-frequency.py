class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        """
        TC: O(nlogn), SC:O(n) where n = len(nums)
        """
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        return sorted(nums, key=lambda x: (freqs[x], -x))
