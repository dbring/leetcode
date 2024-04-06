class Solution:
    def maxProfitTopDown(self, k: int, prices: list[int]) -> int:
        """
        Top Down Dynamic Programming
        TC:O(nk), SC:O(nk) where n = len(prices)
        """
        dp = {}

        def find_max_profit(day, can_buy, num_tx):
            if (day, can_buy, num_tx) in dp:
                return dp[(day, can_buy, num_tx)]

            if day == len(prices) or num_tx == k:
                return 0

            if can_buy:
                # buy
                dp[(day, can_buy, num_tx)] = (
                    find_max_profit(day + 1, not can_buy, num_tx) - prices[day]
                )
            else:
                # sell
                dp[(day, can_buy, num_tx)] = (
                    find_max_profit(day + 1, not can_buy, num_tx + 1) + prices[day]
                )

            # skip
            skip = find_max_profit(day + 1, can_buy, num_tx)
            dp[(day, can_buy, num_tx)] = max(dp[(day, can_buy, num_tx)], skip)

            return dp[(day, can_buy, num_tx)]

        return find_max_profit(0, True, 0)
