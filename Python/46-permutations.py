class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        https://leetcode.com/problems/permutations/
        TC: O(n * n!) SC: O(n) where n = len(nums)
        TC explanation: n to copy a permutation to the result list, n!
        permutations to generate.
        SC explanation: recursion stack height is n.
        """
        permutations = []

        def find_permutations(permutation):
            if len(permutation) == len(nums):
                permutations.append(permutation.copy())
                return

            for num in nums:
                if num in permutation:
                    continue
                permutation.append(num)
                find_permutations(permutation)
                permutation.pop()

        find_permutations([])
        return permutations
