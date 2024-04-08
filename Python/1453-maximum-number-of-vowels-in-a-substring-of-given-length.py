class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        TC: O(n), SC:O(1) where n = len(s)
        """
        max_vowels = float("-inf")
        vowels = set(["a", "e", "i", "o", "u"])
        vowels_in_window = 0

        for right in range(len(s)):
            char = s[right]

            if char in vowels:
                vowels_in_window += 1

            if right < k:
                max_vowels = max(max_vowels, vowels_in_window)
                continue

            if s[right - k] in vowels:
                vowels_in_window -= 1

            max_vowels = max(max_vowels, vowels_in_window)

        return max_vowels
