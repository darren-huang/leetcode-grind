"""2:35pm - 2:40pm"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0

        for i in range(len(s)):
            # even palindromes, center @ i-1 and i
            l, r = i - 1, i
            while l >= 0 and r < len((s)) and s[l] == s[r]:
                l -= 1
                r += 1
                counter += 1

            # odd palindromes, center @ i
            l, r = i, i
            while l >= 0 and r < len((s)) and s[l] == s[r]:
                l -= 1
                r += 1
                counter += 1

        return counter
