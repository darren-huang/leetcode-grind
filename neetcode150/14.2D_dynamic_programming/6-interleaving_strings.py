"""4:16pm ish
4:26pm"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        seen = {}

        def recurse(s1, s2, s3):
            key = (s1, s2, s3)
            if key in seen:
                return seen[key]

            # base case
            if not s1:
                return s2 == s3
            if not s2:
                return s1 == s3

            # recurrant relation
            ret = (s1[0] == s3[0] and recurse(s1[1:], s2, s3[1:])) or (
                s2[0] == s3[0] and recurse(s1, s2[1:], s3[1:])
            )
            seen[key] = ret
            return ret

        return recurse(s1, s2, s3)
