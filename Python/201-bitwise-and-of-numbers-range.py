class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        TC: O(1), SC: O(1) since left and right are 32-bit integers.
        """
        while left < right:
            right &= right - 1
        return left & right
