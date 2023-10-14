# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        from collections import deque

        queue = deque()

        if root:
            queue.append(root)

        right_side_view = []

        while queue:
            length = len(queue)

            for i in range(length):
                node = queue.popleft()

                if i == length - 1:
                    right_side_view.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return right_side_view
