class CircularQueuek:
    def __init__(self, k: int):
        self.queue = [0 for _ in range(k)]
        self.k = k
        self.front = 0
        self.rear = -1
        self.length = 0

    def enQueue(self, value):
        if self.length < self.k:
            self.length = self.length +1
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = value
            return True
        return False

    def deQueue(self):
        if self.length > 0 :
            self.front = (self.front + 1) % self.k
            self.length = self.length -1
            return True
        return False    

    def Front(self):
        if self.length > 0 :
            return self.queue[self.front]
        return -1

    def Rear(self):
        if self.length > 0:
            return self.queue[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.k