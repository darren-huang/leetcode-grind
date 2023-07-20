#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'computePrices' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER_ARRAY p
#  3. INTEGER_ARRAY q
#


def computePrice(sorted_sp, q):
    # print(sorted_sp, q)
    left, right = 0, len(sorted_sp) - 1
    highest_index = -1
    while left <= right:
        mid = (left + right) // 2
        s, p = sorted_sp[mid]
        if s == q:
            return p
        elif s < q:
            highest_index = mid
            left = mid + 1
        else:  # q < s
            right = mid - 1
    if highest_index != -1:
        return sorted_sp[highest_index][1]
    else:
        raise ValueError("proper s not found for q")


def computePrices(s, p, q):
    sorted_sp = sorted(zip(s, p))
    return [computePrice(sorted_sp, q_) for q_ in q]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    p = list(map(int, input().rstrip().split()))

    k = int(input().strip())

    q = []

    for _ in range(k):
        q_item = int(input().strip())
        q.append(q_item)

    res = computePrices(s, p, q)

    fptr.write("\n".join(map(str, res)))
    fptr.write("\n")

    fptr.close()
