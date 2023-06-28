from typing import List

NUM_LET = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def solution(digits: str):
    temp_word = []
    combinations = []

    def dfs(i):
        # base case
        if i == len(digits):
            if temp_word:
                combinations.append("".join(temp_word))
            return
        dig = digits[i]
        for c in NUM_LET[dig]:
            temp_word.append(c)
            dfs(i + 1)
            temp_word.pop()

    dfs(0)
    return combinations


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return solution(digits)
