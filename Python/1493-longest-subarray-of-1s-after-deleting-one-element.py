class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        """
        TC: O(n), SC:O(1) where n = len(nums).
        Window is monotonically increasing.
        """
        num_zeroes_in_window = 0
        left = 0
        right = 0

        while right < len(nums):
            if nums[right] == 0:
                num_zeroes_in_window += 1

            if num_zeroes_in_window > 1:
                if nums[left] == 0:
                    num_zeroes_in_window -= 1

                left += 1

            right += 1

        return right - left - 1
