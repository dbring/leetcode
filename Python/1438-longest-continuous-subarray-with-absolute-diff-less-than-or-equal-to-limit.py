class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        TC: O(n), SC: O(n)
        """
        from collections import deque

        max_queue = deque()  # monotonically decreasing from left to right
        min_queue = deque()  # monotonically increasing from left to right

        longest_subarray = 0

        left = 0
        for right in range(len(nums)):
            while max_queue and nums[right] > max_queue[-1]:
                max_queue.pop()

            max_queue.append(nums[right])

            while min_queue and nums[right] < min_queue[-1]:
                min_queue.pop()

            min_queue.append(nums[right])

            while abs(max_queue[0] - min_queue[0]) > limit:
                if max_queue[0] == nums[left]:
                    max_queue.popleft()

                if min_queue[0] == nums[left]:
                    min_queue.popleft()

                left += 1

            longest_subarray = max(longest_subarray, right - left + 1)

        return longest_subarray
