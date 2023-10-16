# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree_recursive_dfs(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        https://leetcode.com/problems/same-tree/
        TC: O(n) SC: O(n) where n is the number of nodes in the smaller of the two trees.
        """
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree_recursive_dfs(
            p.left, q.left
        ) and self.isSameTree_recursive_dfs(p.right, q.right)

    def isSameTree_iterative_dfs(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        stack = [(p, q)]

        while stack:
            a, b = stack.pop()

            if not a and not b:
                continue

            if not a or not b or a.val != b.val:
                return False

            stack.append((a.left, b.left))
            stack.append((a.left, b.left))

        return True
