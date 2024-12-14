class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        """
        TC: O(n), SC: O(n) where n = len(s)
        """
        chars = []
        spaces_idx = 0

        for i in range(len(s)):
            if spaces_idx < len(spaces) and i == spaces[spaces_idx]:
                chars.append(" ")
                spaces_idx += 1

            chars.append(s[i])

        return "".join(chars)
