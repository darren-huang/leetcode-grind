"""11:27 - 11:28 - using set

11:33am - constant time finish"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast_pointer = head.next
        slow_pointer = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            if (
                fast_pointer.next == slow_pointer
                or fast_pointer.next.next == slow_pointer
            ):
                return True
            fast_pointer = fast_pointer.next.next

        return False
