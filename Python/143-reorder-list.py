# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Input: head of linked list
# Output: void, modify LL in-place
# Constraints: modify in-place
# Edge cases: null input
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # split list in half
        slow, fast = head, head.next

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if not slow:
            return

        second = slow.next
        slow.next = None

        # reverse second half
        prev = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next

        second = prev

        # merge reversed second half into first half
        current = head
        while current and second:
            next_current = current.next
            current.next = second
            next_second = second.next
            second.next = next_current
            current = next_current
            second = next_second
