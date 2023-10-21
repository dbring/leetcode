class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """
        https://leetcode.com/problems/find-the-duplicate-number/
        TC: O(n), SC: O(1)
        Floyd's algorithm
        """
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
