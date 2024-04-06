class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        """
        TC: O(n), SC:O(1) or O(n) if we include the result space, where n = len(candies)
        """
        max_candies = max(candies)
        result = []

        for candy in candies:
            result.append(candy + extraCandies >= max_candies)

        return result
