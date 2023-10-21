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
