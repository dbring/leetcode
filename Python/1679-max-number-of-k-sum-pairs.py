class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        """
        TC: O(n), SC:O(n)
        """
        from collections import defaultdict

        seen = defaultdict(int)
        num_operations = 0

        for num in nums:
            diff = k - num

            if seen[diff] > 0:
                num_operations += 1
                seen[diff] -= 1
            else:
                seen[num] += 1

        return num_operations

    def maxOperationsSorting(self, nums: list[int], k: int) -> int:
        """
        TC: O(nlogn), SC: O(n)
        """
        nums.sort()

        left = 0
        right = len(nums) - 1
        num_operations = 0

        while left < right:
            sum = nums[left] + nums[right]

            if sum < k:
                left += 1
            elif sum > k:
                right -= 1
            else:
                num_operations += 1
                left += 1
                right -= 1

        return num_operations
