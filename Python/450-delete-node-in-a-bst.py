# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        """
        TC: O(n), SC:O(1) where n is the number of nodes in the tree
        """
        dummy = TreeNode(val=-1, right=root)

        def find_node_to_delete_and_parent():
            parent = dummy
            node_to_delete = root

            while node_to_delete:
                if node_to_delete.val == key:
                    return node_to_delete, parent

                parent = node_to_delete

                if key < node_to_delete.val:
                    node_to_delete = node_to_delete.left
                else:
                    node_to_delete = node_to_delete.right

            return None, parent

        node, parent = find_node_to_delete_and_parent()

        if node is None:
            return root

        left_tree = node.left
        right_tree = node.right

        # replace node
        if parent.left == node:
            if right_tree:
                parent.left = right_tree
            else:
                parent.left = left_tree
                return dummy.right
        else:
            if right_tree:
                parent.right = right_tree
            else:
                parent.right = left_tree
                return dummy.right

        # tack on the left tree to the right tree
        cur = right_tree
        while cur:
            if cur.left:
                cur = cur.left
            else:
                cur.left = left_tree
                break

        return dummy.right
