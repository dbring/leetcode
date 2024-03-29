# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        """
        https://leetcode.com/problems/balanced-binary-tree/

        TC: O(n), SC: O(h) where n is the number of nodes in the tree
        and h is the height of the tree, and h = n in the worst case.
        """
        is_balanced = True

        def tree_height(node):
            nonlocal is_balanced

            if not node:
                return 0

            left_height = tree_height(node.left)
            right_height = tree_height(node.right)

            if abs(left_height - right_height) > 1:
                is_balanced = False

            return 1 + max(left_height, right_height)

        tree_height(root)
        return is_balanced
