class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        TC: O(n), SC: O(1) where n = len(s)
        Space is O(1) because s contains only upper and lowercase letters
        """

        def get_counts(s):
            counts = {}

            for char in s:
                counts[char] = counts.get(char, 0) + 1

            return counts

        counts = get_counts(s)

        has_odd_count = False
        longest_palindrome = 0

        for count in counts.values():
            if count % 2 == 0:
                longest_palindrome += count
            else:
                longest_palindrome += count - 1
                has_odd_count = True

        return longest_palindrome + 1 if has_odd_count else longest_palindrome
