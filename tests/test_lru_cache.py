from src.lru_cache import LRUCache


def test_lru_cache():
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)

    assert cache.get(1) == 1
    assert cache.get(2) == 2

    cache.put(3, 3)

    assert cache.get(1) is None

    cache.put(2, 4)

    assert cache.get(2) == 4

    cache.put(4, 4)

    assert cache.get(3) is None
