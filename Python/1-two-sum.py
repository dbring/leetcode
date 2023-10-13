class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        https://leetcode.com/problems/two-sum/description/
        TC: O(n) SC: O(n), n = len(nums)
        """
        complements = {}  # target - num : index of num

        for index, num in enumerate(nums):
            if num in complements:
                return [index, complements[num]]
            complements[target - num] = index

        return [-1, -1]
