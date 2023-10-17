# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor_iterative_pointer(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        """
        https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
        TC: O(n) SC:O(1)
        """
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root

    def lowestCommonAncestor_recursive_dfs(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        """
        TC: O(n), SC: O(n)
        """
        p_and_q_on_the_right = p.val > root.val and q.val > root.val
        p_and_q_on_the_left = p.val < root.val and q.val < root.val

        if p_and_q_on_the_right:
            return self.lowestCommonAncestor_recursive_dfs(root.right, p, q)
        elif p_and_q_on_the_left:
            return self.lowestCommonAncestor_recursive_dfs(root.left, p, q)
        else:
            return root
