class UnionFind:
    def __init__(self, n):
        self.id = list(range(n))

    def union(self, u, v):
        self.id[self.find(u)] = self.find(v)
    
    def find(self, x):
        # path compression
        if self.id[x] != x:
            self.id[x] = self.find(self.id[x])

        return self.id[x]
