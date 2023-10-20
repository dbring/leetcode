# Definition for a Node.
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        """
        https://leetcode.com/problems/copy-list-with-random-pointer/
        TC: O(n), SC: O(n) where n is the number of nodes in the linked list.
        """
        clones = {None: None}

        current = head
        while current:
            clones[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            clone = clones[current]
            clone.next = clones[current.next]
            clone.random = clones[current.random]
            current = current.next

        return clones[head]
