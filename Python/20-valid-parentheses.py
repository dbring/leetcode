class Solution:
    def isValid(self, s: str) -> bool:
        """
        TC: O(n) SC: O(n), n = len(str)
        """
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}

        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if not stack:
                    return False

                open_bracket = stack.pop()
                if brackets[open_bracket] != c:
                    return False

        return not stack
