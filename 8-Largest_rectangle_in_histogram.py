"""11:00am start

finish coding 11:23am
finish fixing 11:44am


maintain a stack

watchout for repeat variables ie.
for i inside another for i
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # def variable setup
        ascending_tuples = []  # (height, index)
        max_area = 0

        def max_check(height):
            nonlocal max_area
            if height > max_area:
                max_area = height

        for i in range(len(heights)):
            h = heights[i]
            max_check(h)

            # update ascending bars
            if ascending_tuples:
                last_height = ascending_tuples[-1][0]
            else:
                last_height = -1
            if h > last_height:
                ascending_tuples.append((h, i))
            elif h < last_height:
                truncate_index = -1
                for j in range(len(ascending_tuples) - 1, -1, -1):
                    temp_h, temp_i = ascending_tuples[j]
                    if h > temp_h:
                        truncate_index = j
                        break
                    else:
                        max_check(temp_h * (i - temp_i))
                new_index = ascending_tuples[truncate_index + 1][1]
                ascending_tuples = ascending_tuples[: truncate_index + 1] + [
                    (h, new_index)
                ]

        # process ascending bars
        for j in range(len(ascending_tuples)):
            temp_h, temp_i = ascending_tuples[j]
            max_check(temp_h * (len(heights) - temp_i))

        return max_area
