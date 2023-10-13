# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        """
        https://leetcode.com/problems/remove-nth-node-from-end-of-list/

        TC: O(m) SC: O(1) where m is the number of nodes in the linked list.
        """
        dummy = ListNode(0, head)
        prev = dummy
        curr = dummy

        for _ in range(n):
            curr = curr.next

        while curr.next:
            prev = prev.next
            curr = curr.next

        prev.next = prev.next.next

        return dummy.next
