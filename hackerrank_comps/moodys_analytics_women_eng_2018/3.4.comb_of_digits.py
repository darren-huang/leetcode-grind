#!/bin/python3
"""using tribonacci method
do matrix exponentiation with tribonacci
this should speed up time (log n) where n is the nth tribonacci num

This also calculates the tribonacci numbers in order, theory meaning we do 
less work at the cost of having to sort

PASSES ALL TESTS!!!!

tribonacci + matrix exponentiation + sorting numbers
brought us close to timeout threshold (11seconds, timeout is 10 seconds)

last time save was caching some of the matrix multiplications
most common matrix multiplication was the squaring the base
in the "power" function. This is used for computing a power
in log N time, but since the base will always be the same,
caching these calls makes it much faster
"""

import os
import datetime
from functools import lru_cache


MOD = (10**9) + 7
IDENT_MX = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]
TRIB_MX = [
    [1, 1, 1],
    [1, 0, 0],
    [0, 1, 0],
]


def matrix_mul(m1, m2):
    """assume 3x3"""
    ret = [[] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            ret[i].append(sum([m1[i][x] * m2[x][j] for x in range(3)]) % MOD)
    return ret


@lru_cache
def _matrix_square(m):
    return matrix_mul(m, m)


def matrix_square(m):
    return _matrix_square(tuple([tuple(arr) for arr in m]))


def power(base, pow):
    answer = IDENT_MX
    while pow > 0:
        if pow & 1 == 1:  # odd
            answer = matrix_mul(answer, base)
            pow -= 1
        else:  # even
            pow >>= 1
            base = matrix_square(base)
    return answer


def solve(a):
    ret_sum = 0
    a = sorted(a)
    curr_matrix = IDENT_MX
    tribonacci_index = 0

    for ai in a:
        if tribonacci_index < ai:
            mul_mx = power(TRIB_MX, ai - tribonacci_index)
            curr_matrix = matrix_mul(curr_matrix, mul_mx)
            tribonacci_index = ai

        ret_sum += curr_matrix[0][0]
        ret_sum %= MOD
    return ret_sum


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")
    input = open("comb_digits_case_11.txt", "r").readline

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    pre = datetime.datetime.now()
    result = solve(a)
    post = datetime.datetime.now()
    print(result, post - pre)

    # fptr.write(str(result) + "\n")

    # fptr.close()
