class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """
        https://leetcode.com/problems/subsets-ii/
        TC: O(n * 2^n) SC: O(n) where n = len(nums)
        """
        nums.sort()
        power_set = []

        def find_subsets(index, subset):
            power_set.append(subset.copy())

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                find_subsets(i + 1, subset)
                subset.pop()

        find_subsets(0, [])
        return power_set
