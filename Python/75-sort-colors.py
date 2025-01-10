class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        TC: O(n), SC:O(1) where n = len(nums)
        Bucket Sort, two passes through nums
        """
        """
        Do not return anything, modify nums in-place instead.
        """
        COLORS = 3

        bucket = [0] * COLORS

        for color in nums:
            bucket[color] += 1

        i = 0
        for color in range(COLORS):
            while bucket[color]:
                bucket[color] -= 1
                nums[i] = color
                i += 1

    def sortColors(self, nums: List[int]) -> None:
        """
        TC: O(n), SC: O(1) where n = len(nums)
        Dutch National Flag algorithm, single pass through nums.
        """
        left = 0
        right = len(nums) - 1

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
            return

        i = 0
        while i <= right:
            if nums[i] == 0:
                swap(i, left)
                left += 1
                i += 1
            elif nums[i] == 2:
                swap(i, right)
                right -= 1
            else:
                i += 1
