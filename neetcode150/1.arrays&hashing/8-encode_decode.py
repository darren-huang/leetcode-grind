"""
2:15pm

finish 2:29pm"""

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        new_strs = []
        for s in strs:
            s = s.replace("\\", "\\\\")
            s = s.replace(",", "\\,")
            new_strs.append(s)
        return ",".join(new_strs)

    def decode(self, str):
        # write your code here
        strs = []
        last_start = 0
        i = 0
        while i < len(str):
            if str[i] == "\\":
                i += 2
                continue
            elif str[i] == ",":
                strs.append(str[last_start:i])
                last_start = i + 1
            i += 1
        if last_start < i:
            strs.append(str[last_start:i])

        final_strs = []
        for s in strs:
            s = s.replace("\\\\", "\\")
            s = s.replace("\\,", ",")
            final_strs.append(s)
        return final_strs
