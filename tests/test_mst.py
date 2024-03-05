from src.kruskal import kruskal
from src.prim import prim


def test_mst():
    graph = {
        0: {1: 4, 7: 8},
        1: {0: 4, 2: 8, 7: 11},
        2: {1: 8, 3: 7, 5: 4, 8: 2},
        3: {2: 7, 4: 9, 5: 14},
        4: {3: 9, 5: 10},
        5: {2: 4, 3: 14, 4: 10, 6: 2},
        6: {5: 2, 7: 1, 8: 6},
        7: {0: 8, 1: 11, 6: 1, 8: 7},
        8: {2: 2, 6: 6, 7: 7}
    }

    assert kruskal(graph) == 37
    assert prim(graph) == 37
