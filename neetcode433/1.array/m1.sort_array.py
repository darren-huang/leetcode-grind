"""11:44am - 11:57pm"""
from typing import List


def merge_sort(arr: List[int], l: int, r: int) -> None:
    size = r - l + 1
    if size <= 1:
        return

    m = (l + r) // 2
    merge_sort(arr, l, m)
    merge_sort(arr, m + 1, r)

    # merge
    ans = []
    p1, p2 = l, m + 1
    while p1 <= m or p2 <= r:
        if p1 <= m and (p2 > r or arr[p1] < arr[p2]):
            ans.append(arr[p1])
            p1 += 1
        else:
            ans.append(arr[p2])
            p2 += 1

    # print(ans)
    p = l
    for x in ans:
        arr[p] = x
        p += 1


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # print("hi")
        merge_sort(nums, 0, len(nums) - 1)
        return nums
