class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        """
        TC: O(n), SC:O(1)
        """
        # Edge case: all numbers are negative
        if all(num < 0 for num in nums):
            return max(nums)

        # Kadane's Algorithm to find max subarray sum
        max_sum = -float("inf")
        current_sum = 0

        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)

            if current_sum < 0:
                current_sum = 0

        # Kadane's Algorithm to find min subarray sum
        min_sum = float("inf")
        current_sum = 0

        for num in nums:
            current_sum += num
            min_sum = min(min_sum, current_sum)
            if current_sum > 0:
                current_sum = 0

        # Explanation: the min subarray sum is contained within nums
        # like this [x, x, x, m, m, m, m, x, x]. The m's show the min
        # subarray. Therefore, the x's are the max subarray in the
        # circular array
        circular_max = sum(nums) - min_sum

        return max(max_sum, circular_max)
