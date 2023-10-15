class Solution:
    def reverseWords(self, s: str) -> str:
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
