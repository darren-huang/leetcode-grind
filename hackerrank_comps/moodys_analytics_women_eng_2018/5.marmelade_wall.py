#!/bin/python3
"""

FINISHED

for each index i
creates 2 intervals of invalid points based on the height of a_i

these intervals can be combined in linear time (easier to combine them separately)
after combining the intervals
we just need to iterate through all inicdes i that AREN'T included 
in these invalid ranges.

The cost for each wall can be computed in linear time as well.

"""

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER t
#  3. INTEGER r
#  4. INTEGER_ARRAY a
#


def get_costs(l, t, r, a):
    costs = []
    window_sum = 0
    window_len = 0
    max_window_len = (t - l + 1) + (t - r + 1)
    for i, ai in enumerate(a):
        window_sum += ai
        window_len += 1
        if window_len > max_window_len:
            window_sum -= a[i - window_len + 1]
            window_len -= 1
        if window_len == max_window_len:
            costs.append(window_sum)

    strong_wall_cost = ((t + l) * (t - l + 1) // 2) + ((t + r) * (t - r + 1) // 2)
    return [strong_wall_cost - c for c in costs]


def overlap(i1, i2):
    return not (i1[1] < i2[0] or i2[1] < i1[0])


def append_merge(intervals, new_interval):
    while intervals and overlap(intervals[-1], new_interval):
        n_int = intervals.pop()
        new_interval = (
            min(new_interval[0], n_int[0]),
            max(new_interval[1], n_int[1]),
        )
    intervals.append(new_interval)


def get_inval_intervals(l, t, r, a):
    left_invervals = deque()
    right_intervals = deque()
    window_len = (t - l + 1) + (t - r + 1)
    for i, ai in enumerate(a):
        if ai > l:
            num_invalid = min(ai, t + 1) - l
            append_merge(left_invervals, (i - (num_invalid - 1), i))
        if ai > r:
            num_invalid = min(ai, t + 1) - r
            append_merge(
                right_intervals,
                (
                    i - (window_len - 1),
                    i + (num_invalid - 1) - (window_len - 1),
                ),
            )
    return left_invervals, right_intervals


def solve(l, t, r, a):
    window_len = (t - l + 1) + (t - r + 1)
    min_cost = float("inf")
    costs = get_costs(l, t, r, a)
    int1, int2 = get_inval_intervals(l, t, r, a)
    for i in range(len(a) - (window_len - 1)):
        while int1 and int1[0][1] < i:
            int1.popleft()
        while int2 and int2[0][1] < i:
            int2.popleft()

        if int1 and int1[0][0] <= i and int1[0][1] >= i:
            continue
        if int2 and int2[0][0] <= i and int2[0][1] >= i:
            continue

        min_cost = min(min_cost, costs[i])
    return min_cost if min_cost != float("inf") else -1


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    l = int(first_multiple_input[1])

    t = int(first_multiple_input[2])

    r = int(first_multiple_input[3])

    a = list(map(int, input().rstrip().split()))

    result = solve(l, t, r, a)

    fptr.write(str(result) + "\n")

    fptr.close()
