"""recursion depth limits"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'invitations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY pairs
#
MOD = (10**9) + 7


def invitations(n, pairs):
    emps = defaultdict(set)  # maps boss - > set(emps)
    has_no_boss = set(range(1, n + 1))
    for boss, emp in pairs:
        has_no_boss.remove(emp)
        emps[boss].add(emp)

    def calc(has_no_boss):
        so_far_len = 1
        num_ways = 1

        for boss in has_no_boss:
            ways_for_this_tree, size = calc(emps[boss])
            perms = (
                math.factorial(so_far_len + size)
                // math.factorial(so_far_len)
                // math.factorial(size)
            ) % MOD
            so_far_len += size
            num_ways = perms * num_ways * ways_for_this_tree % MOD
        return num_ways, so_far_len

    return int(calc(has_no_boss)[0])


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")
    input = open("party_invitations_test0.txt", "r").readline

    tc = int(input().strip())

    for tc_itr in range(tc):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        pairs = []

        for _ in range(m):
            pairs.append(list(map(int, input().rstrip().split())))

        result = invitations(n, pairs)
        print(result)

    #     fptr.write(str(result) + "\n")

    # fptr.close()
