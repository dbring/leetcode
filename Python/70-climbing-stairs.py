class Solution:
    def climbStairs(self, n: int) -> int:
        """
        TC: O(n), SC: O(1)
        """
        back_two = 1
        back_one = 1

        for _ in range(2, n + 1):
            cur = back_one + back_two
            back_two = back_one
            back_one = cur

        return back_one
