class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
        TC: O(n + w * m) where n = len(sentence), w = len(words),
        m = len(searchWord)
        SC: O(n)
        """
        words = sentence.split(" ")

        for i, word in enumerate(words):
            if word[: len(searchWord)] == searchWord:
                return i + 1

        return -1
