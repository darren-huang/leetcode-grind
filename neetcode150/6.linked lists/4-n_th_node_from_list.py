"""10:14pm - 10:22am


adding a dummy node can help with base case"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer_n_m_1 = (-1, None)
        pointer_n = l_pointer = (0, head)
        while l_pointer[1]:
            if l_pointer[0] - pointer_n[0] + 1 > n:
                pointer_n_m_1, pointer_n = pointer_n, (
                    pointer_n[0] + 1,
                    pointer_n[1].next,
                )
            l_pointer = (l_pointer[0] + 1, l_pointer[1].next)

        if l_pointer[0] - pointer_n[0] < n:
            return head
        if pointer_n[1] == head:
            return head.next
        else:
            pointer_n_m_1[1].next = pointer_n[1].next
            return head
