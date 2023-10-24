# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        from collections import deque

        if not root:
            return []

        largest_values = []
        queue = deque([root])

        while queue:
            row_length = len(queue)

            max_row_val = float("-inf")

            for _ in range(row_length):
                node = queue.popleft()
                max_row_val = max(max_row_val, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            largest_values.append(max_row_val)

        return largest_values
