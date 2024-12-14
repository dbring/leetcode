class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's Algorithm
        TC: O(n), SC: O(1) where n = len(nums)
        """
        prev_subarray_sum = float("-inf")
        max_subarray_sum = float("-inf")

        for num in nums:
            if prev_subarray_sum < 0:
                prev_subarray_sum = 0

            prev_subarray_sum += num
            max_subarray_sum = max(max_subarray_sum, prev_subarray_sum)

        return max_subarray_sum
