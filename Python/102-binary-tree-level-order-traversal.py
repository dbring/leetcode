# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """
        https://leetcode.com/problems/binary-tree-level-order-traversal/

        TC: O(n), SC: O(n) where n is the number of nodes in the tree.
        """
        from collections import deque

        queue = deque()

        if root:
            queue.append(root)

        level_order = []

        while queue:
            level = []
            length = len(queue)

            for _ in range(length):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level_order.append(level)

        return level_order
