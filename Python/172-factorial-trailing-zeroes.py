class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        TC: O(logn), SC:O(1)
        """
        count_of_trailing_zeroes = 0

        while n:
            n //= 5
            count_of_trailing_zeroes += n

        return count_of_trailing_zeroes
