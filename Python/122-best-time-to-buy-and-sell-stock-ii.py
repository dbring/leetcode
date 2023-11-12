class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        TC: O(n), SC:O(1) where n = len(prices)
        """
        buy = 0
        max_profit = 0

        for sell in range(len(prices)):
            if prices[sell] > prices[buy]:
                max_profit += prices[sell] - prices[buy]
            buy = sell

        return max_profit
