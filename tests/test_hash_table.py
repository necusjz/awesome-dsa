from src.hash_table import HashTable


def test_hash_table():
    ht = HashTable()

    ht.insert(10, "Alice")
    ht.insert(25, "Bob")
    ht.insert(20, "Charlie")

    assert ht.get(10) == "Alice"
    assert ht.get(25) == "Bob"
    assert ht.get(20) == "Charlie"
    assert ht.get(30) is None

    ht.insert(25, "David")

    assert ht.get(25) == "David"

    ht.remove(10)

    assert ht.get(10) is None
    assert ht.get(20) == "Charlie"
    assert ht.get(25) == "David"
