class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        TC: O(n), SC: O(1) where n = len(s)
        """
        window = set()
        length_of_longest_substring = 0
        left = 0

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])
            length_of_longest_substring = max(
                length_of_longest_substring, right - left + 1
            )

        return length_of_longest_substring
