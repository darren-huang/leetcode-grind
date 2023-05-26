"""11:12am - 11:20am

forgot to update something"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(None)
        new_pointer = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            new_pointer.next = ListNode(carry % 10)
            new_pointer = new_pointer.next
            carry = carry // 10
        
        return dummy.next
