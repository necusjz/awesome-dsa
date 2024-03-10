from heapq import heappush, heappop


def prim(graph):
    min_heap = [(0, 0)]
    visited = set()

    dist = 0
    while len(visited) < len(graph):
        w, u = heappop(min_heap)
        if u in visited:
            continue

        visited.add(u)
        dist += w

        for v in graph[u]:
            heappush(min_heap, (graph[u][v], v))

    return dist
