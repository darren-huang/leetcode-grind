"""
DO NOT PUT [] or {} AS DEFAULT ARGUMENTS
"""


class Trie:
    class TrieNode:
        def __init__(self, char) -> None:
            self.char = char
            self.children = {}
            self.is_word = False

    def __init__(self):
        self.root = Trie.TrieNode(None, None)

    def insert(self, word: str) -> None:
        pointer = self.root
        for c in word:
            if c not in pointer.children:
                pointer.children[c] = Trie.TrieNode(c)
            pointer = pointer.children[c]
        pointer.is_word = True

    def search(self, word: str) -> bool:
        pointer = self.root
        for c in word:
            if c not in pointer.children:
                return False
            pointer = pointer.children[c]
        return pointer.is_word

    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        for c in prefix:
            if c not in pointer.children:
                return False
            pointer = pointer.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
