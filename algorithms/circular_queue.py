class CircularQueue:
    def __init__(self, k: int):
        self.queue = [-1 for _ in range(k + 1)]
        self.size = k + 1
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.tail - 1 + self.size) % self.size]
        
    def isEmpty(self) -> bool:
        if self.head == self.tail:
            return True
        return False

    def isFull(self) -> bool:
        if (self.tail + 1) % self.size == self.head:
            return True
        return False
