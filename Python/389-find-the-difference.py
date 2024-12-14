class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        TC: O(n), SC:O(1) where n = len(s)
        """
        ALPHABET_SIZE = 26
        s_count = [0] * ALPHABET_SIZE
        t_count = [0] * ALPHABET_SIZE

        for char in s:
            s_count[ord(char) - ord("a")] += 1

        for char in t:
            t_count[ord(char) - ord("a")] += 1

        for i in range(ALPHABET_SIZE):
            if s_count[i] != t_count[i]:
                return chr(i + ord("a"))
