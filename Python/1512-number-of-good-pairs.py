from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        """
        TC: O(n), SC: O(n), n = len(nums)
        """
        counts = defaultdict(int)
        good_pairs = 0

        for num in nums:
            good_pairs += counts[num]
            counts[num] += 1

        return good_pairs

    def numIdenticalPairs_bruteforce(self, nums: list[int]) -> int:
        """
        TC: O(n^2), SC: O(1), n = len(nums)
        """
        good_pairs = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] != nums[j]:
                    continue
                good_pairs += 1

        return good_pairs
