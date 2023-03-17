from collections import defaultdict


class TrieNode:
    """Manipulate its children and determine if it's a word."""
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr_node = self.root
        for w in word:
            curr_node = curr_node.children[w]

        curr_node.is_word = True

    def search(self, word):
        curr_node = self.root
        for w in word:
            curr_node = curr_node.children.get(w)
            if not curr_node:
                return False

        return curr_node.is_word
