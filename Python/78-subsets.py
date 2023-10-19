class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        https://leetcode.com/problems/subsets/
        TC: O(n * 2^n), SC: O(n) where n = len(nums)
        TC explanation: n to copy the subset into the power_set and 2^n
        recursive calls in the decision tree.
        SC explanation: max depth of the recursion stack is the length of nums.
        """
        power_set = []

        def find_subsets(index, subset):
            if index == len(nums):
                power_set.append(subset[:])
                return

            find_subsets(index + 1, subset)
            subset.append(nums[index])
            find_subsets(index + 1, subset)
            subset.pop()

        find_subsets(0, [])
        return power_set
