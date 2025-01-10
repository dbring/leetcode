# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """
        TC: O(n), SC: (n)
        """
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        NULL = "#"
        node_vals = []

        def dfs(node):
            if not node:
                node_vals.append(NULL)
                return

            node_vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(node_vals)

    def deserialize(self, data):
        """
        TC: O(n), SC: O(n)
        """
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        NULL = "#"
        node_vals = data.split(",")
        index = 0

        def dfs():
            nonlocal index

            if node_vals[index] == NULL:
                index += 1
                return None

            node = TreeNode(int(node_vals[index]))

            index += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
