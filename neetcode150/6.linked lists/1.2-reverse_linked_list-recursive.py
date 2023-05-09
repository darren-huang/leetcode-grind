"""
11:33 start ish?
11:42 finish

recursion remember to check which variables you are updating with
ie. return & variables to make recursive call (ie. iteration vars)
check return types!
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_helper(head):
    """returns start AND end"""
    if head.next is None:
        return head, head

    r_first, r_last = reverse_helper(head.next)
    r_last.next = head
    head.next = None

    return r_first, head


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        first, _ = reverse_helper(head)
        return first
