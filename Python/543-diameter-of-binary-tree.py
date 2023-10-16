# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        """
        https://leetcode.com/problems/diameter-of-binary-tree/description/

        TC: O(n) SC: O(h) where n is the number of nodes in the tree
        and h is the height of the tree, and h = n in the worst case.
        """
        diameter = 0

        def find_diameter(node):
            nonlocal diameter

            if not node:
                return 0

            left = find_diameter(node.left)
            right = find_diameter(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        find_diameter(root)

        return diameter
