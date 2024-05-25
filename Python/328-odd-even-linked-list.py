# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        """
        TC: O(n), SC: O(1)
        """
        if not head:
            return head

        even_sentinel = ListNode()

        prev = head
        cur = head.next
        e = even_sentinel

        while cur:
            e.next = cur
            prev.next = cur.next
            prev = prev.next if prev.next else prev
            cur = cur.next.next if cur.next else None
            e = e.next

        e.next = None
        prev.next = even_sentinel.next

        return head
