#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'numbersSquare' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER s
#


def numbersSquare(n, s):
    sq = [[0] * n for _ in range(n)]
    curr = s
    for i in range(n):
        for j in range(i + 1):
            sq[j][i] = curr
            curr += 1
        for j in range(i - 1, -1, -1):
            sq[i][j] = curr
            curr += 1
    for row in sq:
        print(" ".join([str(i) for i in row]))


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    s = int(first_multiple_input[1])

    numbersSquare(n, s)
