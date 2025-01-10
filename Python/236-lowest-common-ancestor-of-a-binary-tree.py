# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Modification of the tree.
        TC: O(n), SC: O(n) where n is the number of nodes in the tree.
        """

        def set_parents(node, parent):
            if not node:
                return

            node.parent = parent

            set_parents(node.left, node)
            set_parents(node.right, node)

        set_parents(root, None)

        def get_ancestors(node):
            cur = node
            ancestors = []

            while cur:
                ancestors.append(cur)
                cur = cur.parent

            return ancestors[::-1]

        p_ancestors = get_ancestors(p)
        q_ancestors = get_ancestors(q)

        lowest_common_ancestor = root

        for i in range(min(len(p_ancestors), len(q_ancestors))):
            if p_ancestors[i] != q_ancestors[i]:
                return lowest_common_ancestor

            lowest_common_ancestor = p_ancestors[i]

        return lowest_common_ancestor

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root

        return l or r
