from src.binary_indexed_tree import BinaryIndexedTree


def test_bit():
    bit = BinaryIndexedTree(10)

    bit.update(3, 6)
    bit.update(5, 8)
    bit.update(7, 10)

    assert bit.query(3) == 6
    assert bit.query(5) == 14  # 6 + 8
    assert bit.query(7) == 24  # 6 + 8 + 10
    assert bit.query(9) == 24
