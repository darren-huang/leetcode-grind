"""Too slow"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#


def get_dist(p, index, val):
    dist = 0
    if index == 0:
        dist += val
    if index > 0:
        dist += abs(val - p[index - 1])
    if index < len(p) - 1:
        dist += abs(val - p[index + 1])
    return dist


def solve(p):
    total_dist = p[0]
    for i in range(len(p) - 1):
        total_dist += abs(p[i] - p[i + 1])

    best_so_far = total_dist

    for i in range(len(p) - 1):
        for j in range(i + 1, len(p)):
            curr_pair_dist = get_dist(p, i, p[i]) + get_dist(p, j, p[j])
            if abs(i - j) == 1:
                curr_pair_dist -= abs(p[i] - p[j])

            # swap i and j, then calc diff
            new_pair_dist = get_dist(p, i, p[j]) + get_dist(p, j, p[i])
            if abs(i - j) == 1:
                new_pair_dist += abs(p[i] - p[j])

            best_so_far = min(best_so_far, total_dist - curr_pair_dist + new_pair_dist)
    return best_so_far


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    p_count = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = solve(p)

    fptr.write(str(result) + "\n")

    fptr.close()
