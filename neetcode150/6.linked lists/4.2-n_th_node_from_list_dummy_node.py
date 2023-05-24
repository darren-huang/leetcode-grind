"""10:25pm


adding a dummy node can help with base case

another idea is having two pointers in the linked list
maintaining some distance between the two
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        p_nm1, i_nm1, i = dummy, -1, 0
        while head:
            if i - i_nm1 > n:
                p_nm1, i_nm1 = p_nm1.next, i_nm1 + 1
            head, i = head.next, i + 1

        # print(p_nm1, i_nm1, i)
        if i - i_nm1 - 1 == n and p_nm1.next:
            p_nm1.next = p_nm1.next.next
        
        return dummy.next
