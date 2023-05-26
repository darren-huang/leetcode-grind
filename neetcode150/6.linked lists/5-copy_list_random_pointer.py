"""
10:40am 10 :46am
# Definition for a Node.
"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        hash2node = {None: None}
        pointer = head
        while pointer:
            hash2node[pointer] = Node(pointer.val)
            pointer = pointer.next

        pointer = head
        while pointer:
            hash2node[pointer].next = hash2node[pointer.next]
            hash2node[pointer].random = hash2node[pointer.random]
            pointer = pointer.next
        
        return hash2node[head]