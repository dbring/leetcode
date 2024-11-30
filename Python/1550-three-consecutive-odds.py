class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        """
        TC: O(n), SC:O(1)
        """
        if len(arr) < 3:
            return False

        for i in range(2, len(arr)):
            left = arr[i - 2]
            middle = arr[i - 1]
            right = arr[i]

            if left % 2 and middle % 2 and right % 2:
                return True

        return False
