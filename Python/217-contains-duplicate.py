class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        https://leetcode.com/problems/contains-duplicate/description/
        TC: O(n) S:O(n)
        """
        distinct_nums = set(nums)
        is_duplicate_in_nums = len(distinct_nums) != len(nums)
        return is_duplicate_in_nums
