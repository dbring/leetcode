class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        https://leetcode.com/problems/combination-sum-ii/
        TC: O(n * 2^n) SC: O(n)
        TC explanation: 2^n possible combinations, n to append the copy.
        SC explanation: stack depth and/or sorting.
        """
        candidates.sort()
        combinations = []

        def find_combinations(index, combination, combination_sum):
            if combination_sum == target:
                combinations.append(combination.copy())
                return

            if combination_sum > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                combination.append(candidates[i])
                find_combinations(i + 1, combination, combination_sum + candidates[i])
                combination.pop()

        find_combinations(0, [], 0)
        return combinations
