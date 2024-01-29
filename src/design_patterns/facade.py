class Array:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.arr = [0] * self.capacity

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            raise IndexError("K is out of bounds!")

        return self.arr[k]

    def append(self, item):
        if self.n == self.capacity:
            self.resize()

        self.arr[self.n] = item
        self.n += 1

    def insert(self, index, item):
        if index < 0 or index > self.n:
            raise IndexError("Please enter appropriate index!")

        if self.n == self.capacity:
            self.resize()

        for i in range(self.n - 1, index - 1, -1):
            self.arr[i+1] = self.arr[i]

        self.arr[index] = item
        self.n += 1

    def pop(self):
        if self.n == 0:
            raise SystemError("Array is empty!")

        self.n -= 1

        return self.arr[self.n]

    def resize(self):
        self.capacity *= 2
        narr = [0] * self.capacity

        for i in range(self.n):
            narr[i] = self.arr[i]

        self.arr = narr
