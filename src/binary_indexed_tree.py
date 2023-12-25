class BinaryIndexedTree:
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & -i  # low bit

    def prefix_sum(self, i):
        ret = 0
        while i:
            ret += self.sums[i]
            i -= i & -i

        return ret
