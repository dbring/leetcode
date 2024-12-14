class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        TC: O(1)
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        TC: O(1) amortized.
        How does this work?
        Push n elements onto the queue (stack1). Then pop from the queue.
        Those n elements are all popped from stack1 and pushed onto stack2.
        This is O(n) time complexity. But every subsequent pop for the
        remaining n - 1 elements is O(1). So this means to pop all
        n elements takes O(n + n - 1) = O(2*n) = O(n) time. So that means
        if we amortize that time complexity across the n elements we
        get an amortized O(1) time complexity.
        """
        if self.stack2:
            return self.stack2.pop()

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self) -> int:
        """
        TC: O(1)
        """
        if self.stack2:
            return self.stack2[-1]

        return self.stack1[0]

    def empty(self) -> bool:
        """
        TC: O(1)
        """
        return not self.stack1 and not self.stack2
