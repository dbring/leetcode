class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        TC: O(m * n), SC: O(m) where m = amount, n = len(coins)
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != float("inf") else -1
