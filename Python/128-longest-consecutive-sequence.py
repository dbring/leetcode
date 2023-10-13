class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        https://leetcode.com/problems/longest-consecutive-sequence/
        TC: O(n) SC:O(1), n = len(nums)
        """
        uniques = set(nums)
        longest_sequence = 0

        for num in nums:
            if num - 1 in uniques:
                continue

            current_sequence_length = 1

            while num + current_sequence_length in uniques:
                current_sequence_length += 1

            longest_sequence = max(longest_sequence, current_sequence_length)

        return longest_sequence
