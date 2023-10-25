class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        https://leetcode.com/problems/k-th-symbol-in-grammar/

        TC: O(n) SC: O(1)
        """
        current_num = 0
        left = 1
        right = 2 ** (n - 1)

        for _ in range(n - 1):
            mid = left + (right - left) // 2

            if mid >= k:
                right = mid
            else:
                left = mid + 1
                current_num = 0 if current_num else 1

        return current_num
