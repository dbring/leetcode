# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        TC: O(n), SC: O(n) where n is the number of nodes in the tree
        """

        def is_valid(node, min, max):
            if not node:
                return True

            if node.val <= min or node.val >= max:
                return False

            is_left_subtree_valid = is_valid(node.left, min, node.val)
            is_right_subtree_valid = is_valid(node.right, node.val, max)

            return is_left_subtree_valid and is_right_subtree_valid

        return is_valid(root, float("-inf"), float("inf"))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        from collections import deque

        queue = deque()
        queue.append((root, float("-inf"), float("inf")))

        while queue:
            node, left, right = queue.pop()

            if not node:
                continue

            if not (left < node.val < right):
                return False

            queue.append((node.left, left, node.val))
            queue.append((node.right, node.val, right))

        return True
