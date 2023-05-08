"""start 12:15pm

1:00pm
disaster

1:07pm
time limit exceeded

1:15pm
finished.... with great regret


defaultdict takes in a function (0 args)! defaultdict(list) or defaultdict(set) works as well
deque works, normal pop append, also popleft appendleft
set().union is NON DESTRUCTIVE remember to set the equal value

When using tuples as keys BE CAREFUL
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)

        pattern_to_set = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "?" + word[i + 1 :]
                pattern_to_set[pattern].add(word)

        def get_neighbors(word):
            neighbors = set()
            for i in range(len(word)):
                pattern = word[:i] + "?" + word[i + 1 :]
                neighbors = neighbors.union(pattern_to_set[pattern])
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
