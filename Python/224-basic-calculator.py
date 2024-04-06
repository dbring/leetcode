class Solution:
    def calculate(self, s: str) -> int:
        """
        TC: O(n), SC:O(n) where n = len(s)
        """
        PLUS = "+"
        MINUS = "-"
        LEFT_PARENTHESIS = "("
        RIGHT_PARENTHESIS = ")"
        stack = []
        current_digit = 0
        sign = 1
        result = 0

        for char in s:
            if char.isdigit():
                current_digit = current_digit * 10 + int(char)

            if char == PLUS or char == MINUS:
                result += current_digit * sign
                current_digit = 0

                if char == PLUS:
                    sign = 1
                else:
                    sign = -1

            if char == LEFT_PARENTHESIS:
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0

            if char == RIGHT_PARENTHESIS:
                result += current_digit * sign
                result *= stack.pop()  # sign
                result += stack.pop()  # previous result
                current_digit = 0

        return result + current_digit * sign
