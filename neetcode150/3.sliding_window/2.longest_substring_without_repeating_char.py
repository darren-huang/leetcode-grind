"""2:37pm
2:45pm

make sure all variables are updated correctly
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_window_len = 0
        chars_set = set()
        window_beginning_pointer = 0
        for window_end_pointer in range(len(s)):
            char = s[window_end_pointer]
            if char in chars_set:
                # remove until no longer in chars_set
                while True:
                    farthest_char = s[window_beginning_pointer]
                    window_beginning_pointer += 1
                    chars_set.remove(farthest_char)
                    if farthest_char == char:
                        break

            chars_set.add(char)
            window_len = window_end_pointer - window_beginning_pointer + 1
            max_window_len = max(max_window_len, window_len)
        return max_window_len
