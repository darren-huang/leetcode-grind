"""
given array
4 3 5 1 2 8 9

take min, remove left and right neighbors
repeat (sum the MINs only)

rm 1 -> (rm 2, 5)
4 3 8 9
rm 3 -> (rm 4, 8)
9
rm 9

total = 13

"""

import heapq
from typing import List, Optional

# create a doubly linked hashmap for neighbor tracking


class DLLNode:
    def __init__(
        self,
        index: Optional[int],
        prev: Optional["DLLNode"] = None,
        next: Optional["DLLNode"] = None,
    ) -> None:
        self.index, self.prev, self.next = index, prev, next


class LinkedHashMap:
    def __init__(self, n: int) -> None:
        # create DLL
        self.sent = DLLNode(None)
        self.sent.next = self.sent.prev = self.sent
        # create hashmap
        self.map = {}  # maps index -> node

        for i in range(n):
            self.add(i)

    def add(self, index: int) -> None:
        """Adds to the end of the DLL & updates  map."""
        # update DLL
        prev, nxt = self.sent.prev, self.sent
        new_node = DLLNode(index, prev=prev, next=nxt)
        prev.next = nxt.prev = new_node  # type: ignore

        # update map
        self.map[index] = new_node

    def remove(self, index: int) -> None:
        """Removes the index, AND adjacent neighbors"""
        # print(f"remove {index}")
        node = self.map[index]
        rm_nodes = [n for n in [node, node.prev, node.next] if n is not self.sent]
        for rm_node in rm_nodes:
            # print(f"\n{rm_node.prev.index}, {rm_node.index}, {rm_node.next.index}")
            # print(f"remove node with index {rm_node.index}")
            # update DLL
            prev, nxt = rm_node.prev, rm_node.next
            prev.next, nxt.prev = nxt, prev

            # update map
            del self.map[rm_node.index]


def solution(arr: List[int]):
    # keep track of original index, which will map to some doubly linked hashmap
    mheap = [(a, i) for i, a in enumerate(arr)]
    lhm = LinkedHashMap(len(arr))
    heapq.heapify(mheap)
    total = 0
    while mheap:
        n_val, n_index = heapq.heappop(mheap)
        if n_index not in lhm.map:
            continue  # if already removed, skip

        # now remove index & update total
        total += n_val
        lhm.remove(n_index)
    return total


def test():
    arr = [4, 3, 5, 1, 2, 8, 9]  # item shifting
    assert solution(arr) == 13
    arr = [1, 100, 5, 100, 2]  # rmv at edges
    assert solution(arr) == 8
    arr = [100, 1, 1]  # tiebreak
    assert solution(arr) == 1
    arr = [5, 4, 3, 2, 1, 2, 3, 4, 5]
    assert solution(arr) == 8

    print("all correct")


if __name__ == "__main__":
    test()
