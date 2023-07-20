#!/bin/python3
"""using tribonacci method
do matrix exponentiation with tribonacci
this should speed up time (log n) where n is the nth tribonacci num
"""

import os
import datetime
from collections import defaultdict

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY a as parameter.
#

MOD = (10**9) + 7


def power(base, pow, multiply=lambda x, y: x * y, identity_val=1):
    answer = identity_val
    while pow > 0:
        if pow % 2 == 1:  # odd
            answer = multiply(answer, base)
            pow -= 1
        else:  # even
            pow //= 2
            base = multiply(base, base)
    return answer


def matrix_mul(m1, m2):
    """assume 3x3"""
    ret = [[] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            ret[i].append(sum([m1[i][x] * m2[x][j] % MOD for x in range(3)]) % MOD)
    return ret


def tribonacci(ai):
    base_matrix = [
        [1, 1, 1],
        [1, 0, 0],
        [0, 1, 0],
    ]  # vector is [1, 0, 0]
    mul_matrix = power(
        base_matrix,
        ai,
        multiply=matrix_mul,
        identity_val=[
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ],
    )
    return mul_matrix[0][0]


def solve(a):
    ret_sum = 0
    for ai in a:
        ret_sum += tribonacci(ai)
        ret_sum %= MOD
    return ret_sum


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")
    input = open("comb_digits_test2.txt", "r").readline

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    pre = datetime.datetime.now()
    result = solve(a)
    post = datetime.datetime.now()
    print(result, post - pre)

    # fptr.write(str(result) + "\n")

    # fptr.close()
