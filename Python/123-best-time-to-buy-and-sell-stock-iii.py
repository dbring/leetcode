class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Top Down Dynamic Programming
        TC:O(n^2), SC:O(n) where n = len(prices)
        """
        dp = {}

        def find_max_profit(day, can_buy, num_tx):
            if (day, can_buy, num_tx) in dp:
                return dp[(day, can_buy, num_tx)]

            if day == len(prices) or num_tx == 2:
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

    def maxProfit(self, prices: list[int]) -> int:
        """
        Finite State Machine
        TC: O(n), SC:O(n)
        """
        from collections import defaultdict

        CAN_BUY, CAN_SELL = 0, 1
        MAX_NUM_TX = 2

        dp = defaultdict(int)  # key: (state, kth-transaction)

        dp[(CAN_SELL, 0)] = float("-inf")
        dp[(CAN_SELL, 1)] = float("-inf")
        dp[(CAN_SELL, 2)] = float("-inf")

        for price in prices:
            # 1st Transaction: skip or sell
            dp[(CAN_BUY, 1)] = max(dp[(CAN_BUY, 1)], dp[(CAN_SELL, 1)] + price)

            # 1st Transaction: skip or buy
            dp[(CAN_SELL, 1)] = max(dp[(CAN_SELL, 1)], dp[(CAN_BUY, 0)] - price)

            # 2nd Transaction: skip or sell
            dp[(CAN_BUY, 2)] = max(dp[(CAN_BUY, 2)], dp[(CAN_SELL, 2)] + price)

            # 2nd Transaction: skip or buy
            dp[(CAN_SELL, 2)] = max(dp[(CAN_SELL, 2)], dp[(CAN_BUY, 1)] - price)

        return dp[(CAN_BUY, MAX_NUM_TX)]
