#!/bin/python3
"""failing many tests"""

import math
import os
import random
import re
import sys
import heapq


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


def validate(cps, k, sorted_qs):
    # print("cps", cps)
    curr_time = sorted_qs[0][0]
    buffer = []  # mheap -> (End Time, amount of time to buffer)
    for start, timeout in sorted_qs:
        # print(start, start + timeout, curr_time, buffer)
        end_time = start + timeout
        # wait from curr_time to start_time, decrease buffer
        if start > curr_time:
            time_to_wait = start - curr_time
            curr_time += time_to_wait

        # do k task, update buffer
        pre_push_time = curr_time
        curr_time += k / cps
        # print("b", buffer)

        # check if we can beat the turnaround time
        if curr_time <= end_time:
            heapq.heappush(buffer, (pre_push_time, end_time, k / cps))
        else:
            # use buffer
            if not use_buffer(
                buffer,
                curr_time,
                start,
                end_time,
                min(curr_time - end_time, k / cps),
            ):
                return False

    # print("true")
    return True


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
