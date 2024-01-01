class BinaryIndexedTree:
    def __init__(self, k):
        self.bit = [0] * (k + 1)
        self.size = k + 1

    def update(self, i, value):
        while i < self.size:
            self.bit[i] += value
            i += i & -i  # low bit

    def query(self, i):
        psum = 0
        while i:
            psum += self.bit[i]
            i -= i & -i

        return psum
