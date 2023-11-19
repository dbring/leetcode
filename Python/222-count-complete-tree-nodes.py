# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        """
        https://leetcode.com/problems/count-complete-tree-nodes/description/

        TC: O((logn)^2) SC: O(logn) where n in the number of nodes in the tree
        """

        def get_height(node: TreeNode | None) -> int:
            if not node:
                return 0
            return 1 + get_height(node.left)

        number_of_nodes = 0
        while root:
            left_height = get_height(root.left)
            right_height = get_height(root.right)

            if left_height == right_height:
                number_of_nodes += 2**left_height
                root = root.right
            else:
                number_of_nodes += 2**right_height
                root = root.left

        return number_of_nodes
