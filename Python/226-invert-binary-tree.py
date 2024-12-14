# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree_recursive_dfs(self, root: TreeNode | None) -> TreeNode | None:
        """
        TC: O(n) SC:O(h) where n is the number of nodes in the tree
        and h is the max height of the tree. In the worst case, h = n.
        """
        if not root:
            return root

        root.left, root.right = root.right, root.left

        self.invertTree_recursive_dfs(root.left)
        self.invertTree_recursive_dfs(root.right)

        return root

    def invertTree_iterative_dfs(self, root: TreeNode | None) -> TreeNode | None:
        """
        TC: O(n) SC: O(h)
        """
        stack = [root]

        while stack:
            node = stack.pop()

            if not node:
                continue

            node.left, node.right = node.right, node.left

            stack.append(node.right)
            stack.append(node.left)

        return root

    def invertTree_bfs(self, root: TreeNode | None) -> TreeNode | None:
        """
        TC: O(n) SC: O(h)
        """
        from collections import deque

        queue = deque()

        queue.append(root)

        while queue:
            node = queue.popleft()

            if not node:
                continue

            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)

        return root
