from collections import defaultdict


class TrieNode:
    """Operate on its children and determine if it's a word."""
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            # without declaring key
            node = node.children[w]
        node.is_word = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.is_word

    def startswith(self, prefix):
        node = self.root
        for w in prefix:
            node = node.children.get(w)
            if not node:
                return False
        # must be a prefix
        return True
