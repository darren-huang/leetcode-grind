"""12:21pm - 12:43pm

a lot of bugs here
keeping track of pointers is hard
needed to print debug


don't need to enqueue or have a stack
you can just use the linked list as a stack
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_just_k(head, k):
    # reverses first k nodes, and returns new head and last and if more than k items in head
    if k == 1 or not head.next:
        return head, head, k == 1

    new_head, last, valid = reverse_just_k(head.next, k - 1)

    if valid:
        head.next, last.next = last.next, head
        return new_head, head, valid
    else:
        return head, None, valid


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        new_head, last, valid = reverse_just_k(head, k)
        if valid:
            last.next = self.reverseKGroup(last.next, k)

        return new_head
