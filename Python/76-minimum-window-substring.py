class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        TC: O(n), SC: O(1) where n = len(s) since len(t) <= len(s).
        Space is O(1) because the characters of s and t are limited
        to the upper and lowercase English alphabet.
        """
        if len(t) > len(s):
            return ""

        def get_counts(s):
            counts = {}

            for char in s:
                counts[char] = counts.get(char, 0) + 1

            return counts

        t_counts = get_counts(t)
        min_win_start = 0
        min_win_end = float("inf")
        window_counts = {}

        def is_t_in_window():
            for char, count in t_counts.items():
                if char not in window_counts:
                    return False

                if window_counts[char] < count:
                    return False

            return True

        left = 0
        for right in range(len(s)):
            if s[right] not in window_counts:
                window_counts[s[right]] = 0

            window_counts[s[right]] += 1

            while is_t_in_window():
                if right - left < min_win_end - min_win_start:
                    min_win_start = left
                    min_win_end = right

                window_counts[s[left]] -= 1
                left += 1

        return s[min_win_start : min_win_end + 1] if min_win_end != float("inf") else ""

    def minWindow(self, s: str, t: str) -> str:
        """
        TC: O(n), SC: O(1)
        This is slightly more efficient since we don't have to check
        the counts each time.
        """
        if len(s) < len(t):
            return ""

        t_counts = {}
        window_counts = {}
        total_t_char_counts = 0
        min_win_start = 0
        min_win_end = float("inf")

        for char in t:
            t_counts[char] = t_counts.get(char, 0) + 1

        total_t_char_counts = len(t_counts)

        left = 0
        window_count_same_as_t = 0

        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in t_counts and window_counts[char] == t_counts[char]:
                window_count_same_as_t += 1

            while window_count_same_as_t == total_t_char_counts:
                if right - left < min_win_end - min_win_start:
                    min_win_start = left
                    min_win_end = right

                window_counts[s[left]] -= 1
                if s[left] in t_counts and window_counts[s[left]] < t_counts[s[left]]:
                    window_count_same_as_t -= 1

                left += 1

        return s[min_win_start : min_win_end + 1] if min_win_end != float("inf") else ""
