from collections import defaultdict, deque
import heapq


def solution(tasks: List[str], n: int):
    # count number of each task (finish when these are all zero
    num_tasks = defaultdict(lambda: 0)
    for t in tasks:
        num_tasks[t] += 1

    # create heapq with waiting times for tasks
    mxheap = [
        (-num_tasks[t], 0, t) for t in num_tasks
    ]  # (time can be done, task, num_left)
    heapq.heapify(mxheap)
    q = deque()

    curr_time = 0
    # loop, get next task that can be done
    while mxheap or q:
        while q and q[0][1] <= curr_time:
            heapq.heappush(mxheap, q.popleft())
        if not mxheap:
            heapq.heappush(mxheap, q.popleft())

        nleft, ntime, ntask = heapq.heappop(mxheap)
        print(curr_time, ntime, ntask, nleft)

        # can i do task right now
        if ntime <= curr_time:
            # yes
            curr_time += 1
        else:
            # no, must be done later
            curr_time = ntime + 1

        nleft += 1
        if nleft < 0:
            q.append((nleft, curr_time + n, ntask))
    return curr_time


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        return solution(tasks, n)
