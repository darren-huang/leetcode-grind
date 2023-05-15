"""11:17am
11:23am
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_start = ListNode(None, None)
        end = dummy_start

        while list1 and list2:
            if list1.val <= list2.val:
                temp_list = list1.next

                # update linked list pointer
                list1.next = None
                end.next = list1

                # update var pointers
                end = list1
                list1 = temp_list
            else:
                temp_list = list2.next

                # update linked list pointer
                list2.next = None
                end.next = list2

                # update var pointers
                end = list2
                list2 = temp_list

        if list1:
            end.next = list1
        elif list2:
            end.next = list2

        return dummy_start.next
