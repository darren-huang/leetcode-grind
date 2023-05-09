#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findTotalWeight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY products as parameter.
#

import heapq


class ProductAndIndex:
    """Create a class to make a weight+index comparable by heapq."""

    def __init__(self, weight, index):
        super().__init__()
        self.weight = weight
        self.index = index

    def __eq__(self, value):
        return (self.weight, self.index) == (value.weight, value.index)

    def __lt__(self, value):
        return (self.weight, self.index) < (value.weight, value.index)

    def __hash__(self):
        return (self.weight, self.index).__hash__()


class LinkedList:
    def __init__(self, prev, val, next) -> None:
        self.prev = prev
        self.val = val
        self.next = next


class LinkedHashmap:
    def __init__(self, list_) -> None:
        self.start = LinkedList(None, None, None)
        self.end = self.start
        self.map_ = {}
        for item in list_:
            new = LinkedList(self.end, item, None)
            self.end.next = new
            self.end = new
            self.map_[item] = new

    def remove(self, item, recurse=False):
        if item in self.map_:
            node = self.map_[item]
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            del self.map_[item]

            if recurse:
                if node.prev is not self.start:
                    self.remove(node.prev.val)
                if node.next:
                    self.remove(node.next.val)


def findTotalWeight(products):
    # first construct the heap and heapify it
    heap = [ProductAndIndex(w, i) for i, w in enumerate(products)]

    # create set to track which items have been removed
    llhm = LinkedHashmap(heap)

    heapq.heapify(heap)

    # loop and continue to pop the min from the heap
    # if a popped item is already removed, skip it
    # keep track of total
    total = 0
    while heap:
        min_item = heapq.heappop(heap)
        if min_item not in llhm.map_:
            continue  # skip items that have been removed
        else:
            # update weight
            total += min_item.weight

            # remove items
            llhm.remove(min_item, recurse=True)
    return total


if __name__ == "__main__":
    print(
        findTotalWeight(
            [
                60,
                21,
                42,
                32,
                12,
                21,
                12,
                63,
                21,
                42,
                32,
                12,
                21,
                12,
                63,
                21,
                42,
                32,
                12,
                21,
                12,
                63,
                21,
                42,
                32,
                12,
                21,
                12,
                63,
                21,
                42,
                32,
                12,
                21,
                12,
                63,
                21,
                42,
                32,
                12,
                21,
                12,
                63,
                21,
                42,
                32,
                12,
                21,
                12,
                63,
                21,
                42,
                32,
                12,
                21,
                12,
                63,
                21,
                42,
                32,
                12,
            ]
        )
    )
