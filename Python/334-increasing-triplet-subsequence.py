class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        """
        TC: O(n), SC:O(1)
        """
        first = float("inf")
        second = float("inf")

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
