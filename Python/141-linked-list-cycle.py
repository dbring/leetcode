class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        """
        TC: O(n), SC:O(1), n = number of nodes in the linked list
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
