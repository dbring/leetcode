class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        """
        TC: O(n), SC:O(n) where n = len(arr)
        """
        seen = set()

        for num in arr:
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True

            seen.add(num)

        return False
