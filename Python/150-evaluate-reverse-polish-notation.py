class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
        TC: O(n), SC: O(n) where n = len(tokens)
        """
        stack = []

        op = {
            "+": lambda x, y: x + y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
            "-": lambda x, y: x - y,
        }

        for token in tokens:
            if token in op:
                y = stack.pop()
                x = stack.pop()
                result = op[token](x, y)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack.pop()
