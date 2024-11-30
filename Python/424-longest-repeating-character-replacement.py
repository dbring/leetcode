class Solution:
    """
    TC O(n), SC:O(1) where n = len(s). Space is O(1) because
    characters of s are uppercase English letters.
    """

    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        longest_substring = 0

        left = 0
        max_freq = 0

        for right in range(len(s)):
            freqs[s[right]] = freqs.get(s[right], 0) + 1

            max_freq = max(max_freq, freqs[s[right]])

            while right - left + 1 - max_freq > k:
                freqs[s[left]] -= 1
                left += 1

            longest_substring = max(longest_substring, right - left + 1)

        return longest_substring
