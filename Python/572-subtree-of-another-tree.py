# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        """
        https://leetcode.com/problems/subtree-of-another-tree/description/

        TC: O(nm) SC: O(n + m) where n is the number of nodes in root, and
        m is the number of nodes in subRoot.
        """
        if not subRoot:
            return True

        if not root:
            return False

        if self.is_same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same_tree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
