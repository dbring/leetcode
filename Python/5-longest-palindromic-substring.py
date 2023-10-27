class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        https://leetcode.com/problems/longest-palindromic-substring/
        TC: O(n^2) SC: O(1) where n = len(s)
        """
        max_length, left_index, right_index = -1, -1, -1

        def palindrome_length(left: int, right: int) -> list[int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return [left + 1, right - 1]

        def update_max(left: int, right: int) -> None:
            nonlocal max_length, left_index, right_index
            if right - left + 1 > max_length:
                max_length = right - left + 1
                left_index = left
                right_index = right

        for i in range(len(s)):
            # check for odd length palindromes
            left, right = palindrome_length(i, i)
            update_max(left, right)

            # check for even length palindromes
            left, right = palindrome_length(i, i + 1)
            update_max(left, right)

        return s[left_index : right_index + 1]
