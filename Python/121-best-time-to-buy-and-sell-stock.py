class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        TC: O(n), SC: O(1) where n = len(prices)
        The thing to realize here is that min_buy should
        monotonically decrease as we iterate
        """
        min_buy = float("inf")
        max_profit = 0

        for sell in prices:
            profit = sell - min_buy
            max_profit = max(max_profit, profit)
            min_buy = min(min_buy, sell)

        return max_profit
