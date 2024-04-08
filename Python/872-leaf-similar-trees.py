# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        TC: O(n + m) where n = nodes in root1 and m = nodes in root2
        SC: O(n + m)
        """

        def find_leaves(node, leaves):
            if not node:
                return

            if not node.left and not node.right:
                leaves.append(node.val)

            find_leaves(node.left, leaves)
            find_leaves(node.right, leaves)

        leaves1 = []
        leaves2 = []

        find_leaves(root1, leaves1)
        find_leaves(root2, leaves2)

        return leaves1 == leaves2
