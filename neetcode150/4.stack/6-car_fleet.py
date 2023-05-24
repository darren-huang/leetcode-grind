"""2:35pm - 2:52pm"""

from typing import List


def car_catch_up(pos1, mph1, pos2, mph2, target):
    """will car1 catch up to car2 before target"""
    if mph1 <= mph2:
        return False

    relative_speed = mph1 - mph2
    distance = pos2 - pos1
    time_to_meet = distance / relative_speed
    meeting_point = (time_to_meet * mph2) + pos2
    return meeting_point <= target


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        num_fleets = 1
        last_car = (
            len(position) - 1
        )  # should be the slowest we are concerned about running into
        sorted_p_s = sorted(zip(position, speed))
        for i in range(len(sorted_p_s) - 2, -1, -1):
            pos, mph = sorted_p_s[i]

            # will car_i catch up to last_car ??
            if car_catch_up(pos, mph, *sorted_p_s[last_car], target):
                continue  # slowest car is "last_car" and no fleets added
            else:
                last_car = i
                num_fleets += 1
        return num_fleets