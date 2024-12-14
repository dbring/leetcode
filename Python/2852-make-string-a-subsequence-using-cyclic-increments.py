class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """
        TC: O(n), SC:O(1) where n = len(str1)
        """
        if len(str1) < len(str2):
            return False

        def next_char(char):
            if char == "z":
                return "a"

            return chr((ord(char) + 1))

        s2 = 0

        for char in str1:
            if s2 < len(str2) and (char == str2[s2] or next_char(char) == str2[s2]):
                s2 += 1

        return s2 == len(str2)
