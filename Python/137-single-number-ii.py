class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        TC: O(n), SC:O(1) where n = len(nums)
        """
        seen_once = 0
        seen_twice = 0

        for num in nums:
            # Add number to seen_once only if not in seen_twice
            # Add number to see_twice only if not in seen_once
            # This throws out all the numbers seen 3 times and keeps
            # the single number in seen_once
            seen_once = (seen_once ^ num) & ~seen_twice
            seen_twice = (seen_twice ^ num) & ~seen_once
        return seen_once
