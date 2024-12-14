from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        TC: O(V + E), SC: O(V) where V = vertices and E = edges
        """
        if not node:
            return node

        clone = {}

        def clone_nodes(node):
            if node in clone:
                return clone[node]

            cloned_node = Node(node.val)
            clone[node] = cloned_node

            for neighbor in node.neighbors:
                cloned_node.neighbors.append(clone_nodes(neighbor))

            return cloned_node

        return clone_nodes(node)
