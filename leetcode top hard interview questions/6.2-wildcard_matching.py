"""Had a few bugs

double check indices that you are iterating over

especially when there is asymmetric interation, double check n vs m,,, s vs p etc.

Double check iteration conditions


"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # init dp arr
        dp_arr = [[None] * (len(p) + 1) for i in range(len(s) + 1)]  # dp_arr[s][p]

        # fill in first row and col
        dp_arr[0][0] = True
        for s_i in range(1, len(s) + 1):
            dp_arr[s_i][0] = False
        for p_i in range(1, len(p) + 1):
            p_char = p[p_i - 1]
            dp_arr[0][p_i] = p_char == "*" and dp_arr[0][p_i - 1]

        # fill out rest of the rows
        for p_i in range(1, len(p) + 1):
            for s_i in range(1, len(s) + 1):
                p_char = p[p_i - 1]
                s_char = s[s_i - 1]
                if p_char == "*":
                    dp_arr[s_i][p_i] = dp_arr[s_i][p_i - 1] or dp_arr[s_i - 1][p_i]
                elif s_char == p_char:
                    dp_arr[s_i][p_i] = dp_arr[s_i - 1][p_i - 1]
                elif p_char == "?":
                    dp_arr[s_i][p_i] = dp_arr[s_i - 1][p_i - 1]
                else:
                    dp_arr[s_i][p_i] = False

        return dp_arr[-1][-1]
