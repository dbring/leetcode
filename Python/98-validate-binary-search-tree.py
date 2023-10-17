# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def is_valid(node, min, max):
            if not node:
                return True

            if node.val <= min or node.val >= max:
                return False

            is_left_subtree_valid = is_valid(node.left, min, node.val)
            is_right_subtree_valid = is_valid(node.right, node.val, max)

            return is_left_subtree_valid and is_right_subtree_valid

        return is_valid(root, float("-inf"), float("inf"))
