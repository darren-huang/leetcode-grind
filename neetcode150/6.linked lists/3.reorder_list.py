"""11:45am - 12pm coding
check 12:03pm finish! 
no mistakes"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        count = 0
        pointer = head
        while pointer:
            count, pointer = count + 1, pointer.next

        middle = (count + 1) // 2  # 4 - > 2 , 3 - > 2

        # get middle linked list
        prev = None
        pointer = head
        for _ in range(middle):
            prev = pointer
            pointer = pointer.next
        if prev:
            prev.next = None

        # reverse middle linked list
        reversed_mid = None
        while pointer:
            temp = pointer.next

            # move pointer link to the front
            pointer.next = reversed_mid
            reversed_mid = pointer

            # update pointer
            pointer = temp

        # interlace reversed with front
        to_interlace = head
        other = reversed_mid
        end = ret = ListNode(None, None)
        while to_interlace and other:
            temp = to_interlace.next

            end.next = to_interlace
            to_interlace.next = None

            end = to_interlace
            to_interlace, other = other, temp

        if to_interlace:
            end.next = to_interlace
        elif other:
            end.next = other

        return ret.next
