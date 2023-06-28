from typing import List


def is_pali(s):
    for j in range(len(s) // 2):
        if s[j] != s[-(1 + j)]:
            return False
    else:
        return True


def solution(s):
    all_combos = []
    curr_combo = []
    curr_pali = s[0]

    def dfs(i):
        nonlocal curr_pali, curr_combo, all_combos
        if i == len(s):
            if is_pali(curr_pali):
                curr_combo.append(curr_pali)
                all_combos.append(curr_combo.copy())
                curr_combo.pop()
            return

        # take current palindrome
        if is_pali(curr_pali):
            # valid palindrome
            curr_combo.append(curr_pali)
            temp = curr_pali
            curr_pali = s[i]

            dfs(i + 1)

            curr_pali = temp
            curr_combo.pop()

        # extend current palindrome
        curr_pali += s[i]
        dfs(i + 1)
        curr_pali = curr_pali[:-1]

    dfs(1)
    return all_combos


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return solution(s)
