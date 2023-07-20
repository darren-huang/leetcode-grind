#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY profits as parameter.
#


def solve(profits):
    dp_dict = {(None, None): 0}  # (alg-2, alg-1): profit
    for algs in profits:
        next_dp_lists = defaultdict(list)
        for (alg_m_2, alg_m_1), c_profit in dp_dict.items():
            for alg_num in range(len(algs)):
                if alg_m_2 == alg_num or alg_m_1 == alg_num:
                    continue
                next_dp_lists[(alg_m_1, alg_num)].append(c_profit + algs[alg_num])
        dp_dict = {key: max(val) for key, val in next_dp_lists.items()}
    return max(dp_dict.values())


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        w = int(input().strip())

        profits = []

        for _ in range(w):
            profits.append(list(map(int, input().rstrip().split())))

        result = solve(profits)

        fptr.write(str(result) + "\n")

    fptr.close()
