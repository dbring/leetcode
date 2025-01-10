class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        https://leetcode.com/problems/permutations/
        TC: O(n * n!) SC: O(n * n!) where n = len(nums)
        TC explanation: n to copy a permutation to the result list, n!
        permutations to generate.
        SC explanation: the output list size.
        """
        permutations = []

        def find_permutations(permutation, used):
            if len(permutation) == len(nums):
                permutations.append(permutation.copy())
                return

            for num in nums:
                if num in used:
                    continue

                permutation.append(num)
                used.add(num)
                find_permutations(permutation, used)
                permutation.pop()
                used.remove(num)

        find_permutations([], set())
        return permutations
