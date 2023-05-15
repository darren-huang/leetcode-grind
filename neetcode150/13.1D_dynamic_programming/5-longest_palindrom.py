"""2:15pm - 2:30pm"""
from collections import deque


class Solution:
    def longestPalindrome(self, s: str) -> str:
        last_palindromes = deque()
        max_pal = ""
        for i in range(0, len(s)):
            for _ in range(len(last_palindromes)):
                prev_palindrome = last_palindromes.popleft()
                other_index = i - len(prev_palindrome) - 1
                if other_index >= 0 and s[i] == s[other_index]:
                    last_palindromes.append(s[i] + prev_palindrome + s[i])
                else:
                    if len(prev_palindrome) > len(max_pal):
                        max_pal = prev_palindrome
            last_palindromes.append(s[i])
            last_palindromes.append("")

        for pal in last_palindromes:
            if len(pal) > len(max_pal):
                max_pal = pal
        return max_pal
