from src.trie import Trie


def test_trie():
    trie = Trie()

    trie.insert("apple")
    trie.insert("app")
    trie.insert("application")
    trie.insert("bear")
    trie.insert("ball")

    assert trie.search("app") is True
    assert trie.search("apps") is False
    assert trie.search("bear") is True
    assert trie.search("application") is True
    assert trie.search("ball") is True
    assert trie.search("b") is False
