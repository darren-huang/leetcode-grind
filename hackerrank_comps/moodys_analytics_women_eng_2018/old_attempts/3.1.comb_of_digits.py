#!/bin/python3
"""failing many tests

uses combinatorics
very slow"""

import math
import os
import random
import re
import sys
from functools import lru_cache

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY a as parameter.
#

MOD = (10**9) + 7


def comb(n2, n4, n8):
    return (
        math.factorial(sum([n2, n4, n8]))
        // math.factorial(n2)
        // math.factorial(n4)
        // math.factorial(n8)
    )


@lru_cache
def solve_ai(ai):
    sum_ = 0
    for n8 in range((ai // 3) + 1):
        for n4 in range(((ai - (n8 * 3)) // 2) + 1):
            n2 = ai - (n8 * 3) - (n4 * 2)
            sum_ += comb(n2, n4, n8)
            sum_ %= MOD
    return sum_


def solve(a):
    # Write your code here
    sum_ = 0
    for ai in a:
        sum_ += solve_ai(ai)
        sum_ %= MOD
    return sum_


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(str(result) + "\n")

    fptr.close()
