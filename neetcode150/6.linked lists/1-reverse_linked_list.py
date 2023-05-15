"""11:11am

11:14am"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        # setup new list, iterate head
        new_head = head
        head = head.next
        new_head.next = None

        while head:
            temp_head = head.next

            # setup the new head with the next item
            head.next = new_head
            new_head = head

            # increment head
            head = temp_head

        return new_head
