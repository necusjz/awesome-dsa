from heapq import heappush, heappop


def prim(graph):
    min_heap = [(0, 0)]
    seen = set()

    dist = 0
    while len(seen) < len(graph):
        w, u = heappop(min_heap)
        if u in seen:
            continue

        seen.add(u)
        dist += w

        for v in graph[u]:
            if v not in seen:
                heappush(min_heap, (graph[u][v], v))

    return dist
