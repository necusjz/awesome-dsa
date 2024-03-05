from union_find import UnionFind


def kruskal(graph):
    edges = []
    for u in graph:
        for v in graph[u]:
            edges.append((graph[u][v], u, v))

    edges.sort()
    uf = UnionFind(len(graph))

    dist = 0
    for w, u, v in edges:
        if uf.find(u) == uf.find(v):
            continue

        uf.union(u, v)
        dist += w

    return dist
