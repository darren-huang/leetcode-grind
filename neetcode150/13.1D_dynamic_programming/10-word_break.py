"""11:00am - 11:09am

no bugs!


woah
okay instead of iterating through words,
make a word SET and do a contains
ie s[i: i + word_len] in word_set
"""
from typing import List
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # record word lengths
        len_to_words = defaultdict(list)
        for word in wordDict:
            len_to_words[len(word)].append(word)

        # record which locations have an existing word sequence
        valid_starts = set([0])  # default is just beginning of str
        for i in range(len(s)):
            # ensure this is a valid start
            if i not in valid_starts:
                continue

            letters_left = len(s) - i
            for word_len, words in len_to_words.items():
                if word_len > letters_left:
                    # word doesn't fit in remaining letters
                    continue
                if i + word_len in valid_starts:
                    # don't need to calculate, this is already valid
                    continue

                # process each word
                for word in words:
                    if s[i : i + word_len] == word:
                        valid_starts.add(i + word_len)
                        break

            # check if we can finish early
            if len(s) in valid_starts:
                return True
        return len(s) in valid_starts
