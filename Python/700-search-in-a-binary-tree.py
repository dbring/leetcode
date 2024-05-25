# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """
        TC: O(logn), SC:O(1)
        """
        cur_node = root

        while cur_node:
            if cur_node.val == val:
                return cur_node

            if val < cur_node.val:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        return cur_node
