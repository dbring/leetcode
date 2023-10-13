class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        TC: O(n) S:O(1) where n = len(prices)
        """
        max_profit = 0
        buy_day = 0
        for sell_day in range(1, len(prices)):
            profit = prices[sell_day] - prices[buy_day]
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                buy_day = sell_day
        return max_profit
