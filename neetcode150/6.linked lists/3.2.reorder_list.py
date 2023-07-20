"""Recursive version"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1 2 3 4
# 1 2 3 4 5
def reorderList(head: Optional[ListNode], index: int, mid: int, even: bool):
    if index == mid:
        if even:
            return head, head.next
        else:
            return head, head

    n_first, n_last = reorderList(head.next, index + 1, mid, even)
    head.next = n_last.next
    n_last.next = head.next.next if head.next else None
    head.next.next = n_first
    return head, n_last


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length, pointer = 0, head
        while pointer:
            length += 1
            pointer = pointer.next
        mid = (length - 1) // 2

        _, last = reorderList(head, 0, mid, length % 2 == 0)
