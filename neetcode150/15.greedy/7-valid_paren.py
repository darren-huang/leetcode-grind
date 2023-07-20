"""11:10am - 11:30am"""
from collections import deque


class Solution:
    def checkValidString(self, s: str) -> bool:
        open_ = deque()
        star = deque()
        for i, c in enumerate(s):
            # print(i, c)
            if c == "(":
                open_.append(i)
            elif c == "*":
                star.append(i)
            else:
                # close
                if open_:
                    open_.pop()
                elif star:
                    star.popleft()
                else:
                    # print(open_, star)
                    print("false 1")
                    return False

        while open_:
            if star:
                if open_[0] < star[0]:
                    open_.popleft()
                star.popleft()
            else:
                # print(open_, star)
                # print("false 2")
                return False
        return True
