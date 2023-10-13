class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        TC: O(n) SC:O(1), n = len(numbers)
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                return [left + 1, right + 1]
            elif two_sum < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]
