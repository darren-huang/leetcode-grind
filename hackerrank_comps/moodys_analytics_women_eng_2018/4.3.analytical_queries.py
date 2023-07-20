#!/bin/python3
"""working passes 55/55 points!"""

import heapq
from collections import deque
from fractions import Fraction


def validate(cps, k, sorted_qs):
    started_tasks = []  # mheap (end_time, amount_left_to_do)
    todo_tasks = deque(sorted_qs)
    curr_time = float("-inf")

    def get_next_todo_start_time():
        if todo_tasks:
            return todo_tasks[0][0]
        else:
            return float("inf")

    while started_tasks or todo_tasks:
        if not started_tasks:
            if curr_time < get_next_todo_start_time():
                curr_time = get_next_todo_start_time()

        while curr_time >= get_next_todo_start_time():
            # get next task
            n_start_time, n_turnaround = todo_tasks.popleft()
            n_end_time = n_start_time + n_turnaround

            # add task to the started tasks
            heapq.heappush(started_tasks, (n_end_time, Fraction(k, cps)))

        # get task to do some work
        curr_end_time, curr_amt_left = heapq.heappop(started_tasks)
        amt_todo = min(get_next_todo_start_time() - curr_time, curr_amt_left)
        curr_time += amt_todo
        curr_amt_left -= amt_todo
        if curr_time > curr_end_time:
            return False
        if curr_amt_left > 0:
            heapq.heappush(started_tasks, (curr_end_time, curr_amt_left))

    return True


def solve(n, k, qs):
    left, right = 1, k
    sorted_qs = sorted(qs)
    lowest_valid = k
    while left <= right:
        mid = (left + right) // 2
        if validate(mid, k, sorted_qs):
            lowest_valid = min(lowest_valid, mid)
            right = mid - 1
        else:
            left = mid + 1
    return lowest_valid


if __name__ == "__main__":
    times_count = int(input().strip())

    for _ in range(times_count):
        n, k = list(map(int, input().rstrip().split()))
        qs = [list(map(int, input().rstrip().split())) for _ in range(n)]

        result = solve(n, k, qs)

        print(result)
