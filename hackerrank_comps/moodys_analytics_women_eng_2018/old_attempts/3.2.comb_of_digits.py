#!/bin/python3
"""using tribonacci method

still too slow"""

import os
from collections import defaultdict

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY a as parameter.
#

MOD = (10**9) + 7


def solve(a):
    a_counts = defaultdict(int)
    for ai in a:
        a_counts[ai] += 1
    max_ai = max(a)
    ret_sum = 0

    # run through tribonacci
    l3, l2, l1 = 0, 0, 1
    for i in range(1, max_ai + 1):
        l3, l2, l1 = l2, l1, sum([l1, l2, l3])
        l1 %= MOD
        if i in a_counts:
            ret_sum += l1 * a_counts[i]
            ret_sum %= MOD
    return ret_sum


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(str(result) + "\n")

    fptr.close()
