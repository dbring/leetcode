class Solution:
    def reverseWords(self, s: str) -> str:
        """
        https://leetcode.com/problems/reverse-words-in-a-string
        TC: O(n) S:O(n) where n = len(s)
        """
        s = s.strip()
        words = []

        word = ""
        for c in s:
            if c == " " and word:
                words.append(word)
                word = ""
                continue
            if c == " " and not word:
                continue
            word += c

        words.append(word)
        return " ".join(words[::-1])
