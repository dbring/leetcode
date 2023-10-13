# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth_recursive_dfs(self, root: TreeNode | None) -> int:
        max_depth = 0

        def find_max_depth(node, current_depth):
            nonlocal max_depth

            if not node:
                max_depth = max(max_depth, current_depth)
                return

            find_max_depth(node.left, current_depth + 1)
            find_max_depth(node.right, current_depth + 1)

        find_max_depth(root, 0)

        return max_depth

    def maxDepth_iterative_dfs(self, root: TreeNode | None) -> int:
        max_depth = 0

        stack = [(root, 0)]

        while stack:
            node, depth = stack.pop()

            if not node:
                max_depth = max(max_depth, depth)
                continue

            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))

        return max_depth

    def maxDepth_bfs(self, root: TreeNode | None) -> int:
        from collections import deque

        queue = deque()
        queue.append((root, 0))
        max_depth = 0

        while queue:
            node, depth = queue.popleft()

            if not node:
                max_depth = max(max_depth, depth)
                continue

            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

        return max_depth
