class CircularQueue:
    def __init__(self, k):
        self.queue = [-1] * (k + 1)
        self.size = k + 1
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        if self.is_full():
            return False

        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.size

        return True

    def dequeue(self):
        if self.is_empty():
            return False

        self.head = (self.head + 1) % self.size

        return True

    def front(self):
        if self.is_empty():
            return -1

        return self.queue[self.head]

    def rear(self):
        if self.is_empty():
            return -1

        return self.queue[(self.tail - 1 + self.size) % self.size]

    def is_empty(self):
        if self.head == self.tail:  # empty or not
            return True

        return False

    def is_full(self):
        if (self.tail + 1) % self.size == self.head:  # full or not
            return True

        return False
