"""4:46pm - 5:48pm

took a while but was doing the linter
and talking to"""
from typing import List


class TrieNode:
    def __init__(self, letter, parent) -> None:
        self.letter = letter
        self.parent = parent
        self.children = {}  # maps letter -> TrieNode
        self.is_word = False
        self.removed = False


def add_word(root: TrieNode, word):
    for c in word:
        if c in root.children:
            root = root.children[c]
        else:
            root.children[c] = TrieNode(c, root)
            root = root.children[c]

    root.is_word = True


def remove_word(root: TrieNode, word):
    node = root
    for c in word:
        node = node.children[c]
    node.is_word = False

    while node.parent and not node.children:
        node.removed = True
        del node.parent.children[node.letter]
        node = node.parent


def get_children(i, j, n, m):
    candidates = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    return [
        (c_i, c_j)
        for c_i, c_j in candidates
        if c_i >= 0 and c_j >= 0 and c_i < n and c_j < m
    ]


def dfs_words(board, trie_root, i, j, n, m):
    visited = set([(i, j)])
    curr_word = board[i][j]
    if curr_word not in trie_root.children:
        return []
    node = trie_root.children[curr_word]

    found_words = set()
    # print(n,m)

    def dfs(i, j):
        nonlocal node, found_words, curr_word, visited
        if node.is_word:
            found_words.add(curr_word)
            remove_word(trie_root, curr_word)
        if node.removed:
            return
        for c_i, c_j in get_children(i, j, n, m):
            # print(c_i,c_j)
            c_char = board[c_i][c_j]
            if c_char in node.children and (c_i, c_j) not in visited:
                # process c_i, c_j
                visited.add((c_i, c_j))
                node = node.children[c_char]
                curr_word += c_char

                # recurse
                dfs(c_i, c_j)

                # unprocess c_i, c_j
                visited.remove((c_i, c_j))
                node = node.parent
                curr_word = curr_word[:-1]

    dfs(i, j)
    return found_words


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # construct trie
        root = TrieNode(None, None)
        for word in words:
            add_word(root, word)

        # use trie as BFS through each node of the grid via backtracking
        ret_set = set()
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                gotten_words = dfs_words(board, root, i, j, n, m)
                ret_set = ret_set.union(gotten_words)

        return list(ret_set)
