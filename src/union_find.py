class UnionFind:
    def __init__(self, n):
        self.id = list(range(n))

    def union(self, u, v):
        self.id[self.find(u)] = self.find(v)
    
    def find(self, u):
        if self.id[u] != u:  # path compression
            self.id[u] = self.find(self.id[u])

        return self.id[u]
