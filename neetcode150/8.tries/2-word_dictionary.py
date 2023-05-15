"""10:07pm took a big break with annie, hopped in call finished like 10:52pm
est. took like 10-20 min

0 mistakes!
stick with the dfs method tho
"""


class WordDictionary:
    class TrieNode:
        def __init__(self, char) -> None:
            self.char = char
            self.children = {}
            self.is_word = False

    def __init__(self):
        self.root = WordDictionary.TrieNode(None)

    def addWord(self, word: str) -> None:
        pointer = self.root
        for c in word:
            if c not in pointer.children:
                pointer.children[c] = WordDictionary.TrieNode(c)
            pointer = pointer.children[c]
        pointer.is_word = True

    def search(self, word: str) -> bool:
        def dfs(i, pointer):
            if i >= len(word):
                if pointer.is_word:
                    return True
                return False

            char = word[i]
            if char == ".":
                for child in pointer.children.values():
                    if dfs(i + 1, child):
                        return True
            elif char in pointer.children:
                if dfs(i + 1, pointer.children[char]):
                    return True

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
