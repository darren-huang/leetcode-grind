"""Got screwed on the return type being a linked list.

Things learned:
heapq methods all start with "heap"
ie. heapify, heappush, heappop

heapq.heapify is IN PLACE and RETURNS NOTHING
you're thinking of heapified (which doesn't exist) think about sort vs sorted

non local pointers my boi

when making a comparable you only need __eq__ and __lt__

if doing destructive changes to a linked list, ordering of when you are doing the destruction MATTERS!!!
"""
import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ComparableListNode:
    def __init__(self, list_node):
        self.list_node = list_node

    @property
    def val(self):
        return self.list_node.val

    @property
    def next(self):
        return ComparableListNode(self.list_node.next)

    def __eq__(self, other):
        return self.list_node.val == other.val

    def __lt__(self, other):
        return self.list_node.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        start_pointer = None
        end_pointer = None

        def append_solution(list_node):
            nonlocal start_pointer, end_pointer
            if start_pointer is None:
                start_pointer = list_node
                end_pointer = list_node
            else:
                end_pointer.next = list_node
                end_pointer = list_node
            end_pointer.next = None

        comparable_lists = [ComparableListNode(list_) for list_ in lists if list_]
        heapq.heapify(comparable_lists)
        while comparable_lists:
            next_list_node = heapq.heappop(comparable_lists)
            if next_list_node.list_node.next:
                heapq.heappush(comparable_lists, next_list_node.next)
            append_solution(next_list_node.list_node)
        return start_pointer


if __name__ == "__main__":
    print(
        Solution().mergeKLists(
            [
                ListNode(1, ListNode(4, ListNode(5))),
                ListNode(1, ListNode(3, ListNode(4))),
            ]
        )
    )
