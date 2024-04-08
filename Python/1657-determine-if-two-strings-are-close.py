class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        TC:O(n), SC: O(1) where n = len(word1)
        since we do an immediately check to ensure both words
        are the same length. Note: sorting is done on a size 26 list.
        """
        ALPHABET_SIZE = 26

        if len(word1) != len(word2):
            return False

        freq1 = [0] * ALPHABET_SIZE
        freq2 = [0] * ALPHABET_SIZE

        for i in range(len(word1)):
            freq1[ord(word1[i]) - ord("a")] += 1
            freq2[ord(word2[i]) - ord("a")] += 1

        # Check that both word1 and word2 have the same characters
        for i in range(ALPHABET_SIZE):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False

        freq1.sort()
        freq2.sort()

        return freq1 == freq2
