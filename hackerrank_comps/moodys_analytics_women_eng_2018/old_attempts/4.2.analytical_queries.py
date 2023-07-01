"""Too complex, splitting node idea

scrapped for 4.3
"""
#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
from collections import deque
from dataclasses import dataclass
from typing import Optional


def use_buffer(mheap_buffer, curr_time, start_time, end_time, time_to_buffer):
    """Returns true if start and end time can be satisfied, otherwise false."""
    while mheap_buffer and time_to_buffer:
        ipp_time, iend_time, iamt_time = heapq.heappop(mheap_buffer)
        usable_time = min(
            iamt_time,
            iend_time - end_time,
            start_time - ipp_time,
        )
        if usable_time <= 0:
            continue
        use_time = min(usable_time, time_to_buffer)
        time_to_buffer -= use_time
        iamt_time -= use_time
        if iamt_time > 0:
            heapq.heappush(mheap_buffer, (iend_time, iamt_time))
    if time_to_buffer > 0:
        return False
    return True


@dataclass
class Process:
    start_time: float
    duration: float
    end_time: float


class DLLN:
    def __init__(self, val, prev=None, next=None):
        self.val, self.prev, self.next = val, prev, next

    def rm(self):
        prv, nxt = self.prev, self.next
        if prv:
            prv.next = nxt
        if nxt:
            nxt.prev = prv

    def add_next(self, val):
        curr, nxt = self, self.next
        new_node = DLLN(val, curr, nxt)
        curr.next = new_node
        if nxt:
            nxt.prev = new_node


class DLL:
    def __init__(self):
        n = DLLN(None)
        n.next, n.prev = n, n
        self.sentinel = n

    def empty(self):
        return self.sentinel.next == self.sentinel

    def first(self) -> Optional[DLLN]:
        if not self.empty():
            return self.sentinel.next
        raise ValueError("Empty")


def validate(cps, k, sorted_qs):
    schedule = DLL()  # each item holds (start_time, duration, end_time)
    for start_time, timeout in sorted_qs:
        end_time = start_time + timeout
        while (
            not schedule.empty()
            and schedule[0].start_time + schedule[0].end_time <= start_time
        ):
            schedule.popleft()
        if not schedule:
            schedule.appendleft(Process(start_time, k / cps, end_time))
        else:
            pass


def solve(n, k, qs):
    l, r = 1, k
    sorted_qs = sorted(qs)
    lowest_valid = k
    while l <= r:
        m = (l + r) // 2
        if validate(m, k, sorted_qs):
            lowest_valid = min(lowest_valid, m)
            r = m - 1
        else:
            l = m + 1
    return lowest_valid


if __name__ == "__main__":
    times_count = int(input().strip())

    for _ in range(times_count):
        n, k = list(map(int, input().rstrip().split()))
        qs = [list(map(int, input().rstrip().split())) for _ in range(n)]

        result = solve(n, k, qs)

        print(result)
