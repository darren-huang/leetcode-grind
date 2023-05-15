"""2:47pm - 3:09pm

fked up on the understanding of the question
substring vs subsequence
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        max_len = 0
        longest_lengths = [0] * (len(text1) + 1)

        for text2_i in range(len(text2)):
            next_diag_val = longest_lengths[0]
            for lli in range(1, len(longest_lengths)):
                text1_i = lli - 1
                next_diag_val, curr_diag_val = longest_lengths[lli], next_diag_val
                if text2[text2_i] == text1[text1_i]:
                    longest_lengths[lli] = curr_diag_val + 1
                    max_len = max(max_len, longest_lengths[lli])
                else:
                    longest_lengths[lli] = max(
                        longest_lengths[lli],
                        longest_lengths[lli - 1],
                        curr_diag_val,
                    )

        return max_len
