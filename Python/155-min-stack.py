class MinStack:
    """
    https://leetcode.com/problems/min-stack/
    TC for all methods is O(1)
    SC for this class is O(n)
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []  # monotonically decreasing stack

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()

        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        self.stack.append((val, self.min))

    def pop(self) -> None:
        self.stack.pop()

        # Reset the min to inf if the stack is empty
        # or whatever min is at the top of the stack
        if not self.stack:
            self.min = float("inf")
        else:
            self.min = self.stack[-1][1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
