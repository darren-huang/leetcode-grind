"""1:09pm 1:22pm"""
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.my_dict = defaultdict(
            list
        )  # key: [(timestamp, value) ->] sorted by timestamp

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ts_vals = self.my_dict[key]

        l, h = 0, len(ts_vals) - 1
        # binary search through list
        while l <= h:
            m = (l + h) // 2
            if timestamp == ts_vals[m][0]:
                return ts_vals[m][1]  # return value
            elif ts_vals[m][0] < timestamp:  # this is a valid timestamp
                l = m
            else:  # not valid
                h = m - 1

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
