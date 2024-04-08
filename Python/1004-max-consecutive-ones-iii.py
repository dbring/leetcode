class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        """
        TC: O(n), SC: O(1) where n = len(nums)
        The size of the window corresponds to the
        max number of 1s. The window size monotonically
        increases.
        """
        num_zeroes_in_window = 0
        left = 0
        right = 0

        while right < len(nums):
            if nums[right] == 0:
                num_zeroes_in_window += 1

            if num_zeroes_in_window > k:
                if nums[left] == 0:
                    num_zeroes_in_window -= 1

                left += 1

            right += 1

        return right - left
