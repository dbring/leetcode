class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        """
        TC: O(m*n), SC: O(n), where m = len(s) and n = len(words)
        """
        WORD_LENGTH = len(words[0])
        SUBSTRING_LENGTH = len(words) * WORD_LENGTH
        word_counts = {}  # word : count
        start_indices = []

        def get_word_counts():
            nonlocal word_counts

            for word in words:
                if word not in word_counts:
                    word_counts[word] = 0

                word_counts[word] += 1

        get_word_counts()

        for left in range(len(s)):
            if left + SUBSTRING_LENGTH > len(s):
                break

            window_counts = {}

            for word_start in range(left, left + SUBSTRING_LENGTH, WORD_LENGTH):
                word = s[word_start : word_start + WORD_LENGTH]

                if word in word_counts:
                    if word not in window_counts:
                        window_counts[word] = 0

                    window_counts[word] += 1
                else:
                    break

            if window_counts == word_counts:
                start_indices.append(left)

        return start_indices
