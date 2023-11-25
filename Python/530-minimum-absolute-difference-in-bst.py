# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode | None) -> int:
        min_diff = float("inf")
        prev = None

        def find_min_diff(node):
            nonlocal min_diff, prev

            if not node:
                return

            find_min_diff(node.left)

            if prev:
                min_diff = min(min_diff, abs(prev.val - node.val))

            prev = node
            find_min_diff(node.right)

        find_min_diff(root)

        return min_diff
