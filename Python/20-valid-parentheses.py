class Solution:
    def isValid(self, s: str) -> bool:
        """
        TC: O(n) SC: O(n), n = len(str)
        """
        stack = []
        parens = {")": "(", "}": "{", "]": "["}

        for paren in s:
            if paren in parens:
                if stack and parens[paren] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(paren)

        return len(stack) == 0
