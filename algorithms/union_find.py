class UnionFind:
    def __init__(self, n):
        self.id = list(range(n))
    
    def find(self, x):
        # path compression
        if self.id[x] != x:
            self.id[x] = self.find(self.id[x])
        return self.id[x]
    
    def union(self, u, v):
        l = self.find(u)
        r = self.find(v)
        self.id[l] = r
