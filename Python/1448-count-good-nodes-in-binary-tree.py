# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes_recursive_dfs(self, root: TreeNode) -> int:
        number_of_good_nodes = 0

        def count_good_nodes(node, current_max):
            nonlocal number_of_good_nodes

            if not node:
                return

            if current_max <= node.val:
                number_of_good_nodes += 1

            current_max = max(current_max, node.val)

            count_good_nodes(node.left, current_max)
            count_good_nodes(node.right, current_max)

        count_good_nodes(root, root.val)

        return number_of_good_nodes

    def goodNodes_iterative_dfs(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        number_of_good_nodes = 0

        while stack:
            node, current_max = stack.pop()

            if node.val >= current_max:
                number_of_good_nodes += 1

            current_max = max(current_max, node.val)

            if node.left:
                stack.append((node.left, current_max))

            if node.right:
                stack.append((node.right, current_max))

        return number_of_good_nodes
