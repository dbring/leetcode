class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        """
        https://leetcode.com/problems/binary-trees-with-factors/
        TC: O(n^2) SC: O(n)
        """
        mod = 10**9 + 7
        arr.sort()
        dp = {num: 1 for num in arr}

        for parent in arr:
            for child in arr:
                if child == parent:
                    break

                child_sibling = parent // child

                if parent % child == 0 and child_sibling in dp:
                    dp[parent] += dp[child] * dp[child_sibling]

        return sum(dp.values()) % mod
