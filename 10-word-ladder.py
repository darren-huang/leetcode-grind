"""start 12:15pm

1:00pm
disaster


"""

from typing import List
from collections import defaultdict, deque


def count_letters(given_word):
    counts = defaultdict(lambda: 0)
    for c in given_word:
        counts[c] += 1
    return counts


def get_counted_letters_key(counted_letters):
    tuples = [tuple(item) for item in sorted(counted_letters.items()) if item[1] > 0]
    return tuple(tuples)


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)

        letters_to_set = defaultdict(
            lambda: set()
        )  # {((a, 2), (b,2)): {"babat", "babac"}}

        for word in wordList:
            counted_letters = count_letters(word)
            for letter in counted_letters:
                counted_letters[letter] -= 1
                letters_to_set[get_counted_letters_key(counted_letters)].add(word)
                counted_letters[letter] += 1

        def get_neighbors(word):
            counted_letters = count_letters(word)
            neighbors = set()
            for letter in counted_letters:
                counted_letters[letter] -= 1
                neighbors = neighbors.union(
                    letters_to_set[get_counted_letters_key(counted_letters)]
                )
                counted_letters[letter] += 1
            neighbors.remove(word)
            return list(neighbors)

        adj_matrix = {word: get_neighbors(word) for word in wordList}

        queue = deque([(beginWord, 0)])
        seen = set([beginWord])
        while queue:
            word, distance = queue.pop()
            print(word, distance)
            if word == endWord:
                return distance + 1

            for neighbor in adj_matrix[word]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.appendleft((neighbor, distance + 1))

        return 0


if __name__ == "__main__":
    Solution().ladderLength(
        "leet", "code", ["lest", "leet", "lose", "code", "lode", "robe", "lost"]
    )
