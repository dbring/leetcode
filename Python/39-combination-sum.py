class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        https://leetcode.com/problems/combination-sum/
        TC: O(T * N^T), SC: O(T) where T = target.
        TC explanation: T from copying the combination into the output. Note
        that the longest combination we can have is T/2 due to the problem
        constraint 2 <= candidates[i] <= 40. For each element in candidates
        we make a decision to skip it or include it in the combination, so N^T.
        SC explanation: the max height of the recursion stack is T/2, we ignore
        the output list space.
        """
        combinations = []

        def find_combinations(index, combination, combination_sum):
            if combination_sum == target:
                combinations.append(combination.copy())
                return

            if index == len(candidates) or combination_sum > target:
                return

            find_combinations(index + 1, combination, combination_sum)

            combination.append(candidates[index])
            combination_sum += candidates[index]
            find_combinations(index, combination, combination_sum)
            combination.pop()
            combination_sum -= candidates[index]

        find_combinations(0, [], 0)
        return combinations
