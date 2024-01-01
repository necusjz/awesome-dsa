from src.union_find import UnionFind


def test_union_find():
    uf = UnionFind(6)

    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(4, 5)

    assert uf.find(0) == uf.find(2)
    assert uf.find(1) != uf.find(3)
    assert uf.find(3) == uf.find(5)
